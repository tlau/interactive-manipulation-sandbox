Installation
==========

```bash
sudo apt-get install python-zmq
```

Description
==========

Forwards ROS messages between two ROS systems.

multi_ros consists of two processes, the multi_ros_child and the
multi_ros_parent. Typically, the multi_ros_child will run as a server on the
robot. It simply waits for configuration requests. When the
multi_ros_parent is run, it sends configuration requests to the multi_ros_child
(using a ZeroMQ request/reply socket). Using configuration requests,
the multi_ros_parent can get a list of topics currently advertised on the
ROS system to which multi_ros_child is connect; it can tell multi_ros_child what
topics to advertise, and it can tell multi_ros_child what topics it should
subscribe to (and forward to the parent).

After multi_ros_parent configures multi_ros_child, the two each wait for
incoming ROS messages on their ROS system, and forward them to each
other over two ZeroMQ pub/sub connections.

Use
=======

For now, both processes are launched and configured by a single script
called multi_ros_pair. This means that they actually run on the same
computer for the moment, but because they use ZeroMQ for communication
they can easily be split and run on different systems. To run multi_ros_child
and multi_ros_parent, do:

```bash
roscd multi_ros
rosrun multi_ros multi_ros_pair http://localhost:11312 http://localhost:11313 config/test.conf
```

Here the first URI is the ROS_MASTER_URI of the "parent" ROS system, and the second uri
is the ROS_MASTER_URI of the "child" ROS system. test.conf is a json file which
specifies what topics to forward, and what prefix the parent should add to the topics.
