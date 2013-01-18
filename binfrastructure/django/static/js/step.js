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

    // We have to initialize the parameters array inside of the constructor otherwise
    // all Step instances will share the same copy of the parameters array
    init: function() {
      this._super();
      this.set('parameters', {});
    },

    setParam: function(name, value) {
      this.parameters[name] = value;
    },

    getParam: function(name) {
      return this.parameters[name];
    },

    type_to_API_mapping: {
            'pickup': 'pick_up_bin_from_locations',
            'dropoff': 'drop_off_bin_at_locations',
            'goto': 'go_to_pose',
            'speak': 'speak',
            'wait': 'wait'
            },

    display_title: function() {
      if (this.type === 'pickup') {
        return 'Pick up from ' + this.display_location(this.getParam('location'));
      } else if (this.type === 'dropoff') {
        return 'Drop off at ' + this.display_location(this.getParam('location'));
      } else if (this.type === 'goto') {
        return 'Go to ' + this.display_pose(this.getParam('pose'));
      } else if (this.type === 'speak') {
        return 'Say "' + this.display_text(this.getParam('text')) + '"';
      } else if (this.type === 'wait') {
        return 'Wait ' + this.display_duration(this.getParam('duration')) + ' ' + this.getParam('time_period');
      }
    },

    display_location: function(loc) {
      if (loc) {
        return loc.get('name');
      } else {
        return '???';
      }
    },

    display_text: function(text) {
      if (text) {
        return text;
      } else {
        return '???';
      }
    },

    display_duration: function(duration) {
      if (duration) {
        return duration;
      } else {
        return '???';
      }
    },

    display_pose: function(pose) {
      if (pose) {
        return '(' + pose.x.toFixed(2) + ', ' + pose.y.toFixed(2) + ')';
      } else {
        return '(?, ?)';
      }
    },

    // Return a javascript object that will be serialized as JSON and sent to the midtier
    toAPI: function() {
      // NOTE: the views/program.js code uses 'location' in spite of the fact
      // that the API operate on lists of locations. The current implementation
      // of this method discards the list-related possibilities.

      var ret = {
        'action': this.type_to_API_mapping[this.type],
        'params': {}
      };

      // Build the the 'params' object expected by the API.
      for (param_key in this.parameters) {
        if (param_key == 'location') {
          // Build a one element array of bin location IDs.
          ret.params.locations = [this.parameters[param_key].id];
        } else {
          // Copy over the key-value pair.
          ret.params[param_key] = this.parameters[param_key]
        }
      }
      return ret;
    },
  });

  return Step;
});
