'''
This class implements access to the ROS functions necessary to actually have impact on the robots. The rest
of the components in the Web application will access the robot through this interface.
'''

# Fail to initialize if the ROS environment is not set-up
import os
ROS_MASTER_URI = os.getenv('ROS_MASTER_URI')
if not ROS_MASTER_URI:
    raise Exception("ROS_MASTER_URI not set. Please set-up ROS environment properly by running 'source /opt/ros/groovy/setup.bash'")
else:
    print "Using ROS_MASTER_URI = %s" % ROS_MASTER_URI

import rosgraph
import rosnode

NODE_NAME = 'rosbif'
NODE_ID = '/rosbif'

_ros_ready = False
def _init_ros():
    # Make sure we do the initialization only once
    global _ros_ready
    if _ros_ready:
        return True

    # Do a safe, non-blocking test to see if we can communicate with the ROS master
    master = rosgraph.Master(NODE_ID)
    try:
        state = master.getSystemState()
    except:
        raise Exception("Unable to communicate with ROS master")

    # If everything looks OK, try importing rospy, etc.
    import rospy
    rospy.init_node( NODE_NAME)
    _ros_ready = True

class Robot:
    def __init__(self):
        '''Perform ROS initializetion'''
        _init_ros()

    def navigate_to_pose(self, x, y):
        '''Navigates the robot to a given position in the map'''

    def ping(self):
        '''
        Tests ROS connection to robot. Returns True if connection to master is successful or False otherwise
        '''
        return rosnode.rosnode_ping('/rosout',max_count=1)

if __name__ == '__main__':
    r = Robot()
    if r.ping():
        print "Success!"
    else:
        print "Failure"
