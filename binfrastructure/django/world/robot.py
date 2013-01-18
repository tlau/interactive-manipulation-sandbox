"""
Implement the API calls to effect the robot.
"""
import logging


logger = logging.getLogger('robot')


class Robot:

    def __init__(self):
        pass

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
        # ...

    def pick_up_bin(self, bin_id_list, **kwargs):
        """
        params: { 'bin_id_list': (list of numbers) }
        """
        # bins = world.models.Bin.objects.filter(id__in=bin_id_list)
        logger.info('action PICK_UP_BIN invoked with bin_id_list=%s'
                    % bin_id_list)
        # ...

    def pick_up_bin_from_locations(self, binloc_id_list, **kwargs):
        """
        params: { 'binloc_id_list': (list of numbers) }
        """
        logger.info('action PICK_UP_BIN_FROM_LOCATIONS invoked with'
                    ' binloc_id_list=%s' % binloc_id_list)

    def drop_off_bin_at_locations(self, binloc_id_list, **kwargs):
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
