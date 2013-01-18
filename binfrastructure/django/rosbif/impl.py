'''
This class implements access to the ROS functions necessary to actually have impact on the robots. The rest
of the components in the Web application will access the robot through this interface.
'''
# HACK: Prepend rospy-from-source location in python path while we work with hacked rospy
import os, sys
ROSPY_SRC='/'.join(os.path.abspath(__file__).split('/')[:-3]) + '/ros/src/ros_comm/clients/rospy/src'
sys.path.insert(0,ROSPY_SRC)

import logging
logger = logging.getLogger('robot')

# Fail to initialize if the ROS environment is not set-up
import os
ROS_MASTER_URI = os.getenv('ROS_MASTER_URI')
if not ROS_MASTER_URI:
    raise Exception("ROS_MASTER_URI not set. Please set-up ROS environment properly by running 'source /opt/ros/groovy/setup.bash'")
else:
    print "Using ROS_MASTER_URI = %s" % ROS_MASTER_URI

import rospy
import rosgraph
import rosnode
import actionlib
import roslib; roslib.load_manifest("executer_actions")
from executer_actions.msg import ExecuteAction, ExecuteGoal

NODE_NAME = 'rosbif'
NODE_ID = '/rosbif'

TIMEOUT = 20     # Timeout, in seconds for actionlib operations
                 # I don't think this is respected by actionlib though ...

_ros_ready = False
__ac = None
def _init_ros():
    logger.debug("INITIALIZING ROS NODE")

    # Make sure we do the initialization only once
    global _ros_ready
    global __ac
    if _ros_ready:
        logger.debug("(ROS NODE WAS READY)")
        return __ac

    # Do a safe, non-blocking test to see if we can communicate with the ROS master
    master = rosgraph.Master(NODE_ID)
    try:
        state = master.getSystemState()
    except:
        raise Exception("Unable to communicate with ROS master")

    # If everything looks OK, try initializing rospy, etc.
    # rospy.init_node( NODE_NAME, anonymous=True, port=33336)
    rospy.init_node( NODE_NAME, anonymous=True)
    _ros_ready = True

    # Create an actionlib client and connect to server
    __ac = actionlib.SimpleActionClient('/executer/execute', ExecuteAction)
    #rc = __ac.wait_for_server(timeout=rospy.Duration( TIMEOUT))
    rc = __ac.wait_for_server()
    if not rc:
        raise Exception("Timeout trying to connect to SMACH Executer server")
    logger.debug("Successfully initiated ROS and actionlib client")
    return __ac

class RobotImpl:
    def __init__(self):
        '''Perform ROS initializetion'''
        self._ac = _init_ros()

    def navigate_to_pose(self, x, y):
        '''Navigates the robot to a given position in the map'''
        goal = ExecuteGoal()
        goal.action = '''
{
    "type": "action"
  , "name": "NavigateToPose"
  , "inputs":
    {
        "frame_id": "/map"
      , "x": %s
      , "y": %s
      , "theta": 0.0
      , "collision_aware": true
    }
}
''' % (x, y)

        self._ac.send_goal(goal)
        finished = self._ac.wait_for_result(rospy.Duration(TIMEOUT))
        if not finished:
            raise Exception("Timeout waiting for actionlib navigate_to_pose action")

        result = self._ac.get_result()
        return result

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
    r = RobotImpl()
    if r.ping():
        print "Ping 1: Success!"
    else:
        print "Ping 1: Failure"
    rospy.sleep(1)
    print "Ping 2: %s" % r.ac_ping()
    rospy.sleep(5)
