from django.db import models
import json
import logging

logger = logging.getLogger('dev')


class Pose(models.Model):
    """A pose is where the robot can navigate to."""
    x = models.FloatField(default=0)
    y = models.FloatField(default=0)
    angle = models.FloatField(default=0)

    def __unicode__(self):
        return u"x=%s y=%s angle=%s" % (self.x, self.y, self.angle)


class BinLocation(models.Model):
    # Length of location name is currently an arbitraty value.
    name = models.CharField(max_length=200, blank=True)

    # Where / how bins can be picked up or droped off.
    pose = models.OneToOneField(Pose)

    # tags...

    def __unicode__(self):
        return self.name

    @property
    def number_of_bins(self):
        return self.bins.count()


class Bin(models.Model):
    # Length of location name is currently an arbitraty value.
    name = models.CharField(max_length=200, blank=True)

    is_empty = models.BooleanField(default=True)

    # invariant: NULL == being moved / out of system
    location = models.ForeignKey(BinLocation, null=True,
                                 related_name='bins',
                                 on_delete=models.SET_NULL)

    # invariant: NULL == use location field
    pose_last_seen = models.ForeignKey(Pose, null=True)
    time_last_seen = models.DateTimeField(null=True)

    # tags...

    def __unicode__(self):
        return self.name


###############################################################################

"""
BIF Actions are modeled as a (action, params) pair, where the "action" is one
of the defined in the API, identifying the function to call, and the "params"
is a stringified JSON object representing the values to be interpreted as the
function parameter(s).

Consider for example this client code, which builds a "api_call" object ready
to be sent to the server.:

  var api_call = {
    action: 'go_to_pose',
    params: {'pose_x': 1.0, 'pose_y': 2.0, 'pose_angle': 3.14}
    }

  var api_call = {
    action: 'pick_up_from_locations',
    params: {'locations': [1,2,3,4]}
    }

  var api_call = {
    action: 'speak',
    params: {'text': 'something'}
    }

  var api_call = {
    action: 'wait',
    params: {'seconds': 2.0}
    }
"""

MAX_LENGTH_PARAMS_STRING = 200

# Maps API call names to clien selected client BIF actions.
# choice[0] : API call name
# choice[1] : web UI name for the action.
API_call_choices = (
    ('pick_up_bin', 'pick_up_bin'),
    ('pick_up_bin_from_locations', 'pick_up_bin_from_locations'),
    ('drop_off_bin_at_locations', 'drop_off_bin_at_locations'),
    ('go_to_pose', 'go_to_pose'),
    ('speak', 'speak'),
    ('wait', 'wait'),
)


class BIFAction(models.Model):
    """
    A BIF Action instance with parameters bound, corresponding to an API call.
    """

    # API function to be called.
    name = models.CharField(max_length=50, choices=API_call_choices)

    # Bound parameters, codified as a stringified JSON.
    params = models.CharField(max_length=MAX_LENGTH_PARAMS_STRING)

    # The program this step corresponds to. NULL means this step
    # is itself a single-step program.
    program = models.ForeignKey('BIFProgram', blank=True, null=True,
                                related_name='steps')

    # The step index (one-based) of this action in its program.
    step_number = models.PositiveIntegerField(default=1)

    @classmethod
    def from_dict(_class, dict_action):
        """Produce an instance from a dict() representation.

        Raises ValueError if data is not good.
        """
        if not ('action' in dict_action and 'params' in dict_action):
            raise ValueError('The dict() needs "action" and "params"')
        if dict_action['action'] not in [c[0] for c in API_call_choices]:
            raise ValueError('bad bif_action "action" name.')
        return _class(name=dict_action['action'],
                      params=json.dumps(dict_action['params']))

    def to_dict(self):
        """Produce a dict() representation of this instance.

        Raises ValueError if data was not good (which would be very seriuos
        'cause the data could have come from the database).
        """
        if self.name not in [c[0] for c in API_call_choices]:
            raise ValueError("bad API call name.")

        params = json.loads(self.params)
        action_dict = {
            'action': self.name,
            'params': params
        }
        return action_dict


class BIFProgram(models.Model):
    """
    BIF program, considered a sequence of BIF Actions.
    """
    name = models.CharField(max_length=200)

    @property
    def step_sequence(self):
        """Return a QuerySet with the BIFAction instances which compose this
        program, ordered as they should be executed."""
        return self.steps.order_by('step_number')

    def replace_step_sequence(self, step_sequence):
        """Allow to replace the step sequence of this program.

        Each element in the "step_sequence" sequence is a BIFAction
        instance, which will be commited to the database if it has not yet been
        save()'d.

        It is to be noted that the BIFActions are not copied, but assigned to
        this program. If these BIFActions correspond to a different program,
        said program would end up empty.
        """
        # Delete current steps.
        for step in self.step_sequence:
            step.delete()
        # Add the new steps.
        for step in step_sequence:
            step.program = self
            step.save()
