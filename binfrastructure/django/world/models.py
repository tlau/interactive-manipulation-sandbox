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
    pickup_dropoff_pose = models.OneToOneField(Pose)

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
BIF Actions are modeled as a (name, params) pair, where the "name" is one of
the defined in the API, identifying the function to call, and the "params" is a
string of space separated values to be interpreted as the function paramter(s).

Each BIF Action is expected to be able to build its arguments from the "params"
string (which is a JSON stringified). As an example, consider a "go_to_pose"
action receiving a params string like "3.0 -2.2 1.5". It should correspond to a
call to

   go_to_pose(Pose(x=3.0, y=-2.2, angle=1.5))

The to_dict() method of a BIFAction produces a dict instance with keys "name"
and "params". The "name" is the API function to invoke; the "params" is a
python object (corresponding to the 'params' JSON object stringified in the
model instance), ready to be passed to that function.

It is to be noted that the "params" string is limited. This is so to simplify
implementation. The maximum length is exposed as MAX_LENGTH_PARAMS_STRING.

PARAMS DESERIALIZATION:

  "...id_list" kind of params string is expected to be an array of ID values
  (what every type they may be).
  It's turned into a list of IDs.

  "pose" kind of params string is expected to be a object with the "x", "y"
  and "angle" values of a Pose instance.
  It's turned into a (non-saved) Pose instance.

  "text" kind of params string are considered to be a single string and
  interpreted as-is.

  "seconds" kind of params string are expected to be a single numeric value.
  It's turned into a float.

This deserialization allows for the client to serialize JSON objects and pass
them on, which is the simplest possible thing. Examples:

  var api_call = {
    name: 'go_to_pose',
    parameters: {x: 1.0, y: 2.0, angle: 3.14}
    }

  var api_call = {
    name: 'pick_up_from_locations',
    parameters: [1,2,3,4]
    }

  var api_call = {
    name: 'speak',
    parameters: 'something'
    }

  var api_call = {
    name: 'wait',
    parameters: 2.0
    }
"""

MAX_LENGTH_PARAMS_STRING = 200

# Maps API call names to clien selected client BIF actions.
# choice[0] : API call name
# choice[1] : web UI name for the action.
API_call_choices = (
    ('pick_up_bin', 'pick_up_bin'),
    ('pick_up_bin_from_location', 'pick_up_bin_from_location'),
    ('drop_off_bin_at_location', 'drop_off_bin_at_location'),
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

    # The program this instruction corresponds to. NULL means this instruction
    # is itself a single-instruction program.
    program = models.ForeignKey('BIFProgram', blank=True, null=True,
                                related_name='instructions')

    # The instruction index (one-based) of this action in its program.
    instruction_number = models.PositiveIntegerField(default=1)

    @classmethod
    def from_dict(_class, dict_action):
        """Produce an instance from a dict() representation.

        Raises ValueError if data is not good.
        """
        if not ('name' in dict_action and 'params' in dict_action):
            raise ValueError('The dict() needs "name" and "params"')
        if dict_action['name'] not in [c[0] for c in API_call_choices]:
            raise ValueError('bad bif_action name.')
        return _class(name=dict_action['name'],
                      params=json.dumps(dict_action['params']))

    def to_dict(self):
        """Produce a dict() representation of this instance.

        Raises ValueError if data was not good (which would be very seriuos
        'cause the data could have come from the database).
        """
        if self.name not in [c[0] for c in API_call_choices]:
            raise ValueError("bad API call name.")

        params = json.loads(self.params)
        if self.name == "go_to_pose":
            params = Pose(**params)

        action_dict = {
            'name': self.name,
            'params': params
        }
        return action_dict


class BIFProgram(models.Model):
    """
    BIF program, considered a sequence of BIF Actions.
    """
    name = models.CharField(max_length=200)

    @property
    def instruction_sequence(self):
        """Return a QuerySet with the BIFAction instances which compose this
        program, ordered as they should be executed."""
        return self.instructions.order_by('instruction_number')

    def replace_instruction_sequence(self, instruction_sequence):
        """Allow to replace the instruction sequence of this program.

        Each element in the "instruction_sequence" sequence is a BIFAction
        instance, which will be commited to the database if it has not yet been
        save()'d.

        It is to be noted that the BIFActions are not copied, but assigned to
        this program. If these BIFActions correspond to a different program,
        said program would end up empty.
        """
        # Delete current instructions.
        for instruction in self.instruction_sequence:
            instruction.delete()
        # Add the new instructions.
        for instruction in instruction_sequence:
            instruction.program = self
            instruction.save()
