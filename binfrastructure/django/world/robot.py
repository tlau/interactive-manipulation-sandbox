"""
Implement the API calls to effect the robot.
"""
import logging
import rosbif.impl

logger = logging.getLogger('robot')


class Robot:

    def __init__(self):
        logger.debug("Initializing the robot proxy.")
        self._impl = rosbif.impl.RobotImpl()

        # # TO NOTE:
        #
        # # This is interesting... uncommenting this few lines (calling the
        # # "ac_ping" method) makes UI the GETs to /world/api/binlocations fail
        # # _each_ time, instead of just the first time. It'll also fail in
        # # individual location queries, which indicates it'll 500 every
        # # request.
        #
        # logger.debug("AC_PINGING THE RobotImple
        # instance...")  r = self._impl.ac_ping() logger.debug("RESULT OF
        # AC_PING: %s" % r)
        #
        # # If this next few lines are uncommented, however, the behavior does
        # # not change (the ping() does return).
        #
        # logger.debug("PINGING THE RobotImple instance...")
        # r = self._impl.ping()
        # logger.debug("RESULT OF PING: %s" % r)

    def speak(self, text='', **kwargs):
        """
        params: { 'text': (string) }
        """
        logger.info('action SPEAK invoked with text=%s' % text)
        # ...

    def wait(self, seconds=0.0, **kwargs):
        """
        params: { 'seconds': (number) }
        """
        logger.info('action WAIT invoked with seconds=%s' % seconds)
        # ...

    def go_to_pose(self, pose={}, **kwargs):
        """
        params: { 'pose': {'x': (number), 'y': (number), 'angle': (number)} }
        """
        logger.info('action GO_TO_POSE invoked with pose=%s' % pose)
        self._impl.navigate_to_pose(pose['x'], pose['y'])

    def pick_up_bin(self, bin_id_list=[], **kwargs):
        """
        params: { 'bin_id_list': (list of numbers) }
        """
        # bins = world.models.Bin.objects.filter(id__in=bin_id_list)
        logger.info('action PICK_UP_BIN invoked with bin_id_list=%s'
                    % bin_id_list)
        # ...

    def pick_up_bin_from_locations(self, binloc_id_list=[], **kwargs):
        """
        params: { 'binloc_id_list': (list of numbers) }
        """
        logger.info('action PICK_UP_BIN_FROM_LOCATIONS invoked with'
                    ' binloc_id_list=%s' % binloc_id_list)

    def drop_off_bin_at_locations(self, binloc_id_list=[], **kwargs):
        """
        params: { 'binloc_id_list': (list of numbers) }
        """
        logger.info('action DROP_OFF_BIN_AT_LOCATIONS invoked with'
                    ' binloc_id_list=%s' % binloc_id_list)


#
# Intantiate and initialize the Robot only once,
# when the system imports this module.
#
robot_proxy = Robot()
