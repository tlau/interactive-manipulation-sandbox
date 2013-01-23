'''
This class implements access to the ROS functions necessary to actually have impact on the robots. The rest
of the components in the Web application will access the robot through this interface.
'''
# HACK: Prepend rospy-from-source location in python path while we work with hacked rospy
import os, sys
ROSPY_SRC='/'.join(os.path.abspath(__file__).split('/')[:-3]) + '/ros/src/ros_comm/clients/rospy/src'
sys.path.insert(0,ROSPY_SRC)

import logging
logger = logging.getLogger('bif.rosbif')

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

TIMEOUT = 10      # Timeout, in 'rospy time' for actionlib operations
                  # I don't think this is respected by actionlib though ...

# Until rospy becomes thread-safe, we need to make sure we initialize only once
_ros_initialized = False
__ac = None

class RobotImpl:
    def __init__(self, port=33330, tcpros_port=33331):
        '''Perform ROS initializetion'''
        self._ac = self._init_ros(port,tcpros_port)

    def _init_ros(self, port=33330, tcpros_port=33331):
        logger.debug("Starting ROS Node initialization")

        # Make sure we do the initialization only once
        global _ros_initialized
        global __ac
        if _ros_initialized:
            logger.warn("ROS Node was already initialized!")
            return __ac
        _ros_initialized = True

        # Do a safe, non-blocking test to see if we can communicate with the ROS master
        master = rosgraph.Master(NODE_ID)
        try:
            state = master.getSystemState()
        except:
            raise Exception("Unable to communicate with ROS master")
        logger.debug("ROS Master is reachable, proceeding with node initialization. Will use ports %d and %d" % (port, tcpros_port))

        # If everything looks OK, try initializing rospy, etc.
        rospy.init_node( NODE_NAME, anonymous=True, port=port, tcpros_port=tcpros_port)
        logger.debug("ROS Node initialized. Proceeding with actionlib client initialization")

        # Create an actionlib client and connect to server
        __ac = actionlib.SimpleActionClient('/executer/execute', ExecuteAction)
        rc = __ac.wait_for_server(timeout=rospy.Duration( TIMEOUT))
        if not rc:
            raise Exception("Timeout trying to connect to SMACH Executer server")
        logger.debug("Successfully initiated ROS and actionlib client")
        return __ac

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
    # Configure standard console logging
    logging.config.dictConfig({
        'version': 1,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            }
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'robot': {
                'handlers': ['console'],
                'propagate': True,
                'level': 'DEBUG'
            },
            'rospy': {
                'handlers': ['console'],
                'propagate': True,
                'level': 'DEBUG'
            }
        }
    })

    # Optional parameter: xmlrpc port
    port = 33330
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    # Simple program that executes 'ping' functions
    r = RobotImpl(port=port,tcpros_port=port+1)
    logger.info("INITIALIZATION FINISHED SUCCESSFULLY")
    rospy.sleep(5)
    '''
    logger.info("Ping 1 (ROS): %s" % r.ping())
    rospy.sleep(1)
    logger.info("Ping 2 (actionlib): %s" % r.ac_ping())
    rospy.sleep(0.5)
    '''
