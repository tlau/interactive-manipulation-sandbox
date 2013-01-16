define([
  'ember',
  'app'
],
function(
  Ember,
  App
) {

  var Step = Ember.Object.extend({
    title: null,
    type: null,
    parameters: [],

    toAPI: function() {
      var type_to_API_mapping = {
        'pickup': 'pick_up_bin_from_locations',
        'dropoff': 'drop_off_bin_at_locations',
        'goto': 'go_to_pose',
        'speak': 'speak',
        'wait': 'wait'
      };

      var ret = {
        'name': type_to_API_mapping[this.type],
        'parameters': this.parameters
      };

      return ret;
    },
  });

  return Step;
});

