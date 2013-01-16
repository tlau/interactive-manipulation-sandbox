import copy, threading, os
from new import classobj
import roslib, rospy, rosgraph

def make_passthrough_message_class(message_type, md5sum):
    '''
    Creates a message class which knows its type, but doesnt serialize
    or deserialize.

    Args:
        message_type (str) : ROS message type.
    '''
    message_class = classobj('t_passthrough_%s' % message_type, (rospy.msg.AnyMsg,), {
        '_type' : message_type,
        '_md5sum' : md5sum
        })
    return message_class

class TopicInfo:
    '''
    Contains information about a single topic.

    This topic may exist on the remote ROS system, the local
    ROS system, or both.
    '''
    def __init__(self, local_topic):
        self.local_topic = local_topic
        self.message_type = None
        self.md5sum = None
        self.subscribers = []
        self.publishers = []
        self.publisher = None
        self.subscriber = None

class RosInterface:
    def __init__(self, ros_master_uri, node_name, user_message_callback=None):
        self._user_message_callback = user_message_callback

        # set the ROS master uri that rospy will use
        os.environ['ROS_MASTER_URI'] = ros_master_uri

        # install an ugly hack to keep us from subscribing to ourselves
        _my_rospy_uri = None
        _orig_rospy_connect_cb = rospy.impl.registration.RegManager._connect_topic_thread
        def _subscribe_hack(self, topic, uri):
            if uri == _my_rospy_uri:
                return
            return _orig_rospy_connect_cb(self, topic, uri)
        
        rospy.impl.registration.RegManager._connect_topic_thread = _subscribe_hack

        rospy.init_node(node_name, anonymous=True)
        
        self._topics = {}
        self._topics_lock = threading.Lock()

        self._node_name = rospy.get_name()

        # create class for interfacing with the ROS master
        caller_id = rospy.get_caller_id()
        self._master = rosgraph.Master(caller_id)
        print 'My URI is: %s' % self._master.lookupNode(caller_id)
        _my_rospy_uri = self._master.lookupNode(caller_id)

    def get_ros_graph(self):
        '''
        Return a dictionary with info for each local topic.
        '''
        graph = {}
        with self._topics_lock:
            for topic in self._topics:
                topic_info = self._topics[topic]
                graph[topic] = {
                    'message_type' : topic_info.message_type,
                    'md5sum' : topic_info.md5sum,
                    'subscribers' : copy.copy(topic_info.subscribers),
                    'publishers' : copy.copy(topic_info.publishers)
                    }
        return graph

    def update_ros_graph(self):
        '''
        Checks the ROS master for list of topics, as well as number of
        subscribers and publishers for each topic.

        This node is ignored when computing the number of publishers and
        subscribers for each topic.
        '''
        # get all topics from the ROS master, and a list of publishers and subscribers for each
        pubs, subs, services = self._master.getSystemState()
        pubs = dict(pubs)
        subs = dict(subs)
        all_local_topics = set.union(set(pubs.keys()), set(subs.keys()))
        print subs

        # get the types of all topics from the ROS master
        topic_types = dict(self._master.getTopicTypes())
        
        with self._topics_lock:
            # clear previous info on local subscribers/publishers
            for topic in self._topics:
                self._topics[topic].subscribers = []
                self._topics[topic].publishers = []

            # update info on publishers
            for topic in all_local_topics:
                if not topic in self._topics:
                    self._topics[topic] = TopicInfo(topic)
                topic_info = self._topics[topic]

                # set the topic's message type (this is just a string)
                topic_info.message_type = topic_types[topic]

                # this is getting the md5sum from the message class, not from the node
                # publishing the topic. we're assuming that it is using the same message
                # definition as we find in our ROS_PACKAGE_PATH
                message_class = roslib.message.get_message_class(topic_info.message_type)
                if message_class is None:
                    rospy.logdebug('Warning: no message class for message type %s' % topic_info.message_type)
                else:
                    topic_info.md5sum = message_class._md5sum

                if topic in pubs:
                    for publishing_node in pubs[topic]:
                        if not publishing_node == self._node_name:
                            topic_info.publishers.append(publishing_node)

                if topic in pubs:
                    for subscribing_node in pubs[topic]:
                        if not subscribing_node == self._node_name:
                            topic_info.subscribers.append(subscribing_node)

    def advertise(self, topic, message_type, md5sum):
        if not topic in self._topics:
            self._topics[topic] = TopicInfo(topic)
        topic_info = self._topics[topic]
        topic_info.message_type = message_type
        topic_info.md5sum = md5sum
        topic_info.message_class = make_passthrough_message_class(message_type, md5sum)

        # only create publisher for topic if we haven't already
        if topic_info.publisher is None:
            message_class = make_passthrough_message_class(message_type, md5sum)
            topic_info.publisher = rospy.Publisher(topic, message_class)

    def subscribe(self, topic, message_type, md5sum):
        if not topic in self._topics:
            self._topics[topic] = TopicInfo(topic)
        topic_info = self._topics[topic]
        topic_info.message_type = message_type
        topic_info.md5sum = md5sum
        topic_info.message_class = make_passthrough_message_class(message_type, md5sum)

        # only create subscriber for topic if we haven't already
        if topic_info.subscriber is None:
            message_class = make_passthrough_message_class(message_type, md5sum)
            topic_info.subscriber = rospy.Subscriber(topic, message_class, self.message_callback, topic)

    def publish(self, topic, msg_data):
        with self._topics_lock:
            if topic not in self._topics:
                rospy.logwarn("Can't publish message on nonexistant topic %s" % topic)
                return
            elif self._topics[topic].publisher is None:
                rospy.logwarn("Can't publish message on topic %s (not advertised)" % topic)
                return

            topic_info = self._topics[topic]
            msg = topic_info.message_class()
            msg._buff = msg_data

            self._topics[topic].publisher.publish(msg)

    def message_callback(self, msg, topic):
        if self._user_message_callback is None:
            return

        self._user_message_callback(msg, topic)
        

               
            
