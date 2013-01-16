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
import actionlib
import roslib; roslib.load_manifest("executer_actions")
from executer_actions.msg import ExecuteAction, ExecuteGoal

NODE_NAME = 'rosbif'
NODE_ID = '/rosbif'

TIMEOUT = 5     # Timeout, in seconds for actionlib operations

_ros_ready = False
__ac = None
def _init_ros():
    # Make sure we do the initialization only once
    global _ros_ready
    if _ros_ready:
        return __ac

    # Do a safe, non-blocking test to see if we can communicate with the ROS master
    master = rosgraph.Master(NODE_ID)
    try:
        state = master.getSystemState()
    except:
        raise Exception("Unable to communicate with ROS master")

    # If everything looks OK, try importing rospy, etc.
    import rospy; globals()['rospy'] = rospy
    rospy.init_node( NODE_NAME, anonymous=True)
    _ros_ready = True

    # Create an actionlib client and connect to server
    global __ac
    __ac = actionlib.SimpleActionClient('/executer/execute', ExecuteAction)
    rc = __ac.wait_for_server(timeout=rospy.Duration( TIMEOUT))
    if not rc:
        raise Exception("Timeout trying to connect to SMACH Executer server")
    print "Successfully initiated ROS and actionlib client"
    return __ac

class Robot:
    def __init__(self):
        '''Perform ROS initializetion'''
        self._ac = _init_ros()

    def navigate_to_pose(self, x, y):
        '''Navigates the robot to a given position in the map'''

    def ping(self):
        '''
        Tests ROS connection to robot. Returns True if connection to master is successful or False otherwise
        '''
        return rosnode.rosnode_ping('/rosout',max_count=1)

    def ac_ping(self):
        '''
        Test a higher level connection by executing a dummy action
        '''
        goal = ExecuteGoal()
        goal.action = '''
{
    "type": "action"
  , "name": "Dummy"
  , "inputs": {}
}
'''
        self._ac.send_goal(goal)
        finished = self._ac.wait_for_result(rospy.Duration(TIMEOUT))
        if not finished:
            raise Exception("Timeout waiting for actionlib Dummy action")

        result = self._ac.get_result()
        return result


if __name__ == '__main__':
    r = Robot()
    if r.ping():
        print "Ping 1: Success!"
    else:
        print "Ping 1: Failure"
    print "Ping 2: %s" % r.ac_ping()
