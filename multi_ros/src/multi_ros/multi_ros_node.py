import threading, zlib, time
import cPickle as pickle
import zmq
import rospy, roslib, roslib.message

from multi_ros.ros_interface import RosInterface

class PublishedTopic:
    def __init__(self):
        self.topic = None
        self.compression = None
        self.bytes_sent = 0
        self.bytes_received = 0
        
class SubscribedTopic:
    def __init__(self):
        self.topic = None
        self.rate = None
        self.compression = None
        self.bytes_sent = 0
        self.bytes_received = 0
        self.last_forwarded_t = None

class MultiRosNode:
    def __init__(self, name, prefix, ros_master_uri, poll_rate=1.0):
        self._name = name
        self._prefix = prefix
        self._ros_master_uri = ros_master_uri
        self._poll_rate = poll_rate        
        self._pub_topics = {}
        self._pub_topics_lock = threading.Lock()
        self._sub_topics = {}
        self._sub_topics_lock = threading.Lock()

        # used to interact the local ROS system
        self._ros_interface = RosInterface(self._ros_master_uri, self._name, self.local_message_callback)

    def run_as_child(self, config_uri, pub_uri, sub_uri):
        '''
        Bind to these addresses.
        '''
        # socket for configuration requests
        self._zmq_context = zmq.Context()

        # socket for publishing messages
        self._zmq_pub_socket = self._zmq_context.socket(zmq.PUB)
        self._zmq_pub_lock = threading.Lock()

        # socket for receiving messages
        self._zmq_sub_socket = self._zmq_context.socket(zmq.SUB)
        self._zmq_sub_socket.setsockopt(zmq.SUBSCRIBE, '')
        
        rospy.loginfo('%s binding to %s for configuring' % (self._name, config_uri))
        self._zmq_config_socket = self._zmq_context.socket(zmq.REP)
        self._zmq_config_socket.bind(config_uri)
        rospy.loginfo('%s binding to %s for publishing' % (self._name, pub_uri))
        self._zmq_pub_socket.bind(pub_uri)
        rospy.loginfo('%s binding to %s for subscribing' % (self._name, sub_uri))
        self._zmq_sub_socket.bind(sub_uri)

        # start thread that publishes remote messages
        self._remote_message_thread = threading.Thread(target=self.remote_message_thread_func)
        self._remote_message_thread.start()

        loop_rate = rospy.Rate(self._poll_rate)
        while not rospy.is_shutdown():
            msg_str = self._zmq_config_socket.recv()
            req = pickle.loads(msg_str)
            cmd = req['COMMAND']
            if cmd == 'GET_TOPIC_LIST':
                self._ros_interface.update_ros_graph()
                rospy.loginfo('Child sending topic list')
                local_topics = self._ros_interface.get_ros_graph()
                self._zmq_config_socket.send(pickle.dumps(local_topics))
            elif cmd == 'ADVERTISE':
                for topic_dict in req['TOPICS']:
                    topic_info = PublishedTopic()
                    topic_info.topic = str(topic_dict['topic'])
                    topic_info.message_type = str(topic_dict['message_type'])
                    topic_info.md5sum = str(topic_dict['md5sum'])
                    topic_info.compression = topic_dict.get('compression', None)
                    rospy.loginfo('%s advertising %s' % (self._name, topic_info.topic))
                    self._ros_interface.advertise(topic_info.topic, topic_info.message_type, topic_info.md5sum)
                    with self._pub_topics_lock:
                        self._pub_topics[topic_info.topic] = topic_info
                self._zmq_config_socket.send(pickle.dumps('OK'))
            elif cmd == 'SUBSCRIBE':
                for topic_dict in req['TOPICS']:
                    topic_info = SubscribedTopic()
                    topic_info.topic = str(topic_dict['topic'])
                    topic_info.message_type = str(topic_dict['message_type'])
                    topic_info.md5sum = str(topic_dict['md5sum'])
                    topic_info.compression = topic_dict.get('compression', None)
                    topic_info.rate = topic_dict.get('rate', None)
                    rospy.loginfo('%s subscribing to %s' % (self._name, topic_info.topic))
                    self._ros_interface.subscribe(topic_info.topic, topic_info.message_type, topic_info.md5sum)
                    with self._sub_topics_lock:
                        self._sub_topics[topic_info.topic] = topic_info
                self._zmq_config_socket.send(pickle.dumps('OK'))
            else:
                rospy.logerr('Unknown command %s' % cmd)
                self._zmq_config_socket.send(pickle.dumps('ERROR'))
            
            loop_rate.sleep()
        
    def run_as_parent(self, config_uri, pub_uri, sub_uri, config_dict):
        '''
        Connect to these addressses.
        '''
        # socket for configuration requests
        self._zmq_context = zmq.Context()

        # socket for publishing messages
        self._zmq_pub_socket = self._zmq_context.socket(zmq.PUB)
        self._zmq_pub_lock = threading.Lock()

        # socket for receiving messages
        self._zmq_sub_socket = self._zmq_context.socket(zmq.SUB)
        self._zmq_sub_socket.setsockopt(zmq.SUBSCRIBE, '')

        rospy.loginfo('%s connecting to %s for configuring' % (self._name, config_uri))
        self._zmq_config_socket = self._zmq_context.socket(zmq.REQ)        
        self._zmq_config_socket.connect(config_uri)
        rospy.loginfo('%s connecting to %s for publishing' % (self._name, pub_uri))
        self._zmq_pub_socket.connect(pub_uri)
        rospy.loginfo('%s connecting to %s for subscribing' % (self._name, sub_uri))
        self._zmq_sub_socket.connect(sub_uri)

        remote_sub_topics = []
        remote_pub_topics = []        
        rospy.loginfo('%s connecting: %s' % (self._name, str(config_dict)))
        for topic_dict in config_dict['topics']:
            remote_topic = str(topic_dict['topic'])
            local_topic = self.remote_to_local_topic(remote_topic)

            message_type = str(topic_dict['message_type'])
            message_class = roslib.message.get_message_class(message_type)
            if 'compression' in topic_dict:
                compression = topic_dict['compression']
            else:
                compresssion = None
            if 'rate' in topic_dict:
                rate = topic_dict['rate']
            else:
                rate = None
            md5sum = str(message_class._md5sum)
            
            remote_sub_topics.append({
                'topic': remote_topic, 'message_type': message_type,
                'md5sum': md5sum, 'compression': compression, 'rate': rate})
            remote_pub_topics.append({
                'topic': remote_topic, 'message_type': message_type,
                'md5sum': md5sum, 'compression': compression})

            sub_topic_info = SubscribedTopic()
            sub_topic_info.topic = local_topic
            sub_topic_info.message_type = message_type
            sub_topic_info.md5sum = md5sum
            sub_topic_info.rate = rate
            sub_topic_info.compression = compression
            self._sub_topics[sub_topic_info.topic] = sub_topic_info

            pub_topic_info = PublishedTopic()
            pub_topic_info.topic = local_topic
            pub_topic_info.message_type = message_type
            pub_topic_info.md5sum = md5sum
            pub_topic_info.compression = compression
            self._pub_topics[pub_topic_info.topic] = pub_topic_info            
            
            # subscribe to the topic on the local ROS system
            rospy.loginfo('%s subscribing to %s' % (self._name, local_topic))
            self._ros_interface.subscribe(local_topic, message_type, md5sum)

            # advertise the topic on the local ROS system
            rospy.loginfo('%s advertising %s' % (self._name, local_topic))
            self._ros_interface.advertise(local_topic, message_type, md5sum)

        # tell the remote to advertise each of the forwarded topics
        command = {'COMMAND': 'ADVERTISE', 'TOPICS': remote_pub_topics}
        self._zmq_config_socket.send(pickle.dumps(command))
        rep = pickle.loads(self._zmq_config_socket.recv())

        # tell the remote to subscribe to each of the forwarded topics
        command = {'COMMAND': 'SUBSCRIBE', 'TOPICS': remote_sub_topics}
        self._zmq_config_socket.send(pickle.dumps(command))
        rep = pickle.loads(self._zmq_config_socket.recv())

        # spin an wait for remote messages to publish
        self.remote_message_thread_func()


    def local_message_callback(self, msg, local_topic):
        '''
        Received a message on the local ROS system. Forward it to the remote system.
        '''
        with self._sub_topics_lock:
            if not local_topic in self._sub_topics:
                rospy.logwarn('%s: Message received on %s but no config info for this topic' % (self._name, local_topic))
                return
            topic_info = self._sub_topics[local_topic]

        current_t = time.time()
        if topic_info.rate is not None:
            if topic_info.last_forwarded_t is not None:
                if (current_t - topic_info.last_forwarded_t)  < (1.0/topic_info.rate):
                    # just forwarded a message on this topic; don't need to forward this one
                    return
        topic_info.last_forwarded_t = current_t
            
        if self._zmq_pub_socket is not None:
            with self._zmq_pub_lock:
                rospy.logdebug('%s forwarding message on topic %s' % (self._name, local_topic))
                if topic_info.compression is None:
                    msg_buf = msg._buf
                elif topic_info.compression == 'zlib':
                    msg_buf = zlib.compress(msg._buff)
                else:
                    rospy.logerr('Unknown compression type %s for topic %s' % (str(topic_info.compression), local_topic))
                    return
                
                rospy.loginfo('Topic: %s  Uncompressed: %d  Compressed: %d' % (local_topic, len(msg._buff), len(msg_buf)))
                remote_topic = self.local_to_remote_topic(local_topic)
                self._zmq_pub_socket.send(pickle.dumps((remote_topic, msg_buf)))

    def remote_message_thread_func(self):
        '''
        Receive messages from the remote ROS system and republish
        them locally.
        '''
        while not rospy.is_shutdown():
            msg_str = self._zmq_sub_socket.recv()
            remote_topic, msg_buf = pickle.loads(msg_str)
            local_topic = self.remote_to_local_topic(remote_topic)
            with self._pub_topics_lock:
                if not local_topic in self._pub_topics:
                    rospy.logwarn('%s received message on unconfigured topic %s' % (self._name, local_topic))
                    continue
                topic_info = self._pub_topics[local_topic]

            if topic_info.compression is None:
                msg_buf = msg._buf
            elif topic_info.compression == 'zlib':
                msg_buf = zlib.decompress(msg_buf)
            else:
                rospy.logerr('Unknown compression type %s for topic %s' % (str(topic_info.compression), local_topic))
                continue

            
            rospy.logdebug('%s publishing message received over link to topic %s' % (self._name, local_topic))
            self._ros_interface.publish(local_topic, msg_buf)

    def remote_to_local_topic(self, remote_topic):
        return self._prefix + remote_topic        

    def local_to_remote_topic(self, local_topic):
        return local_topic[len(self._prefix):]

