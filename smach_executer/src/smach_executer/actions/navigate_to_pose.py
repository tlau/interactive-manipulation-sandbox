'''
Action for moving the base. Mostly copied from sushi/pr2_python/base.py
'''
import rospy
import actionlib
import tf.transformations as trans
import geometry_msgs.msg as gm
import move_base_msgs.msg as mbm
from smach import State
from actionlib_msgs.msg import GoalStatus
import subprocess
import math

class NavigateToPose(State):
    """
    Navigates to a 2d pose.  Possible outcomes:
    
    * 'succeeded'  In this case, the robot is guaranteed to be at the goal pose.
    * 'failed' Robot not necessarily at the goal pose.
    * 'preempted' Goal was preempted.
    * 'error' Serious error occurred.
    """
    
    def __init__(self, input_keys=['frame_id', 'x', 'y', 'theta', 'collision_aware']):
        move_base_uri = '/move_base'
        self.move_base_node_name = rospy.get_param('move_base_node_name', '/move_base_node')
        self.move_base_client = actionlib.SimpleActionClient(move_base_uri, mbm.MoveBaseAction)
        rospy.loginfo("waiting for move base server")
        self.move_base_client.wait_for_server()
        rospy.loginfo("move base server found")
        self.cmd_vel_pub = rospy.Publisher("base_controller/command", gm.Twist)
        State.__init__(self, outcomes = ['succeeded', 'failed', 'preempted', 'error'], input_keys = input_keys)

    def execute(self, userdata):
        frame_id = userdata['frame_id']
        x = userdata['x']
        y = userdata['y']
        theta = userdata['theta']
        try:
            collision_aware = userdata['collision_aware']
        except KeyError:
            rospy.loginfo("setting missing input collision_aware to True")
            collision_aware = True
        
        #switch global and local planners and costmap params for move_base to be collision-aware or not
        reconfig_str = "rosrun dynamic_reconfigure dynparam set " + self.move_base_node_name 
        if collision_aware:
            rospy.loginfo("navigate_to_pose: switching to collision-aware nav planners")
            move_base_config = ''' "{'base_global_planner': 'navfn/NavfnROS', 'base_local_planner': 'dwa_local_planner/DWAPlannerROS'}" '''
            
            costmap_config = '''/local_costmap "{'max_obstacle_height': 2.0, 'inflation_radius': 0.55 }" '''
            error = subprocess.call(reconfig_str + move_base_config, shell=True)
            if error:
                rospy.logerr("navigate_to_pose: dynamic reconfigure for move_base_node failed!")
                return 'error'
            error = subprocess.call(reconfig_str + costmap_config, shell=True)
            if error:
                rospy.logerr("navigate_to_pose: dynamic reconfigure for costmap_config failed!")
                return 'error'

            goal = mbm.MoveBaseGoal()
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.header.frame_id = frame_id
            goal.target_pose.pose = _to_pose(x, y, theta)

            rospy.loginfo("Sending base goal (%f, %f, %f) and waiting for result" % (x, y, theta))
            self.move_base_client.send_goal(goal)

            r = rospy.Rate(10)
            while not rospy.is_shutdown():
                if self.preempt_requested():
                    self.move_base_client.cancel_goal()
                    self.service_preempt()
                    return 'preempted'
                state = self.move_base_client.get_state()
                if state == GoalStatus.SUCCEEDED:
                    rospy.loginfo("navigation succeeded")
                    return 'succeeded'
                elif state not in [GoalStatus.PENDING, GoalStatus.ACTIVE]:
                    rospy.loginfo("state was:"+str(state))
                    return 'failed'
                r.sleep()

        #non-collision-aware version just sends commands to the base controller for awhile
        else: 
            #only use for small, base-relative commands!  
            if frame_id not in ['base_link', 'base_footprint', '/base_link', '/base_footprint']:
                rospy.logerr("non-collision-aware commands should be in base_link or base_footprint!")
                return 'failed'
            if abs(x) > 0.5:
                rospy.logerr("x was too large, clipping to 0.5 m")
                x = 0.5*x/abs(x)
            if abs(y) > 0.5:
                rospy.logerr("y was too large, clipping to 0.5 m")
                y = 0.5*y/abs(y)

            #send constant-speed commands until (in theory) we could have traveled that far
            time = max([abs(x)/.2, abs(y)/.2, abs(theta)/.25])
            r = rospy.Rate(10)
            steps = int(math.floor(time*10))
            for i in range(steps):
                if self.preempt_requested():
                    return 'preempted'
                base_cmd = gm.Twist()
                base_cmd.linear.x = 10.*x/steps
                base_cmd.linear.y = 10.*y/steps
                base_cmd.angular.z = 10.*theta/steps
                self.cmd_vel_pub.publish(base_cmd)
                r.sleep()

            return 'succeeded'

    def request_preempt(self):
         State.request_preempt(self)
         rospy.loginfo("NavigateToPose was preempted")


def _yaw(q):
    e = trans.euler_from_quaternion([q.x, q.y, q.z, q.w])
    return e[2]

def _to_quaternion(yaw):
    return gm.Quaternion(*trans.quaternion_from_euler(0, 0, yaw))

def _to_pose(x, y, theta):
    return gm.Pose(gm.Point(x, y, 0), _to_quaternion(theta))
