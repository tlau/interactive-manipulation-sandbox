from django.db import models


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

Each BIF Action is expected to be able to build its arguments form the "params"
string. As an example, consider a "go_to_pose" action receiving a params string
like "3.0 -2.2 1.5". It should correspond to a call to

   go_to_pose(Pose(x=3.0, y=-2.2, angle=1.5))

The arguments() method of a BIFAction produces a dict instance with keys "name"
and "arguments". The "name" is the API function to invoke; the "arguments" is a
python object, ready to be passed to that function.

It is to be noted that the "params" string is limited. This is so to simplify
implementation. The maximum length is exposed as MAX_LENGTH_PARAMS_STRING.

PARAMS DESERIALIZATION:

  "...id_list" kind of params string is expected to be ID values (what every
  type) separated by single-space characters.
  Examples: "1 2 3" "'hi hola bonasera' 'chau bye adio'" "[1,2,3]"
  It's turned into a list of those ID values.

  "pose" kind of params string is expected to be three consecutive numeric
  values separated by single-space characters. This are interpreted as "x", "y"
  and "angle" values of a Pose instance.
  It's turned into a (non-saved) Pose instance.

  "text" kind of params string are considered to be a single string and
  interpreted as-is.

  "seconds" kind of params string are expected to be a single numeric value.
  It's turned into a float.
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

    name = models.CharField(max_length=50, choices=API_call_choices)
    params = models.CharField(max_length=MAX_LENGTH_PARAMS_STRING)

    def argument(self):
        """Translate the params string into arguments for the API call."""
        if self.name not in [c[0] for c in API_call_choices]:
            raise ValueError("bad API call name.")

        if self.name in ['pick_up_bin',
                         'pick_up_bin_from_location',
                         'drop_of_bin_at_location']:
            # string of single-space separated IDs.
            return [ID for ID in self.params.split(' ')]
        if self.name == 'go_to_pose':
            # three values, single-space separated.
            x, y, angle = self.params.split(' ')
            return Pose(x=x, y=y, angle=angle)
        if self.name == 'speak':
            # a text string.
            return self.params
        if self.name == 'wait':
            # a single numeric value.
            seconds = float(self.params)
            return seconds

    def translate(self):
        """Produce a dict() representation of this instance."""
        return {
            'name': self.name,
            'arguments': self.argument()
        }
