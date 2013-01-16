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
        return 'Go to ' + this.display_location(this.getParam('location'));
      } else if (this.type === 'speak') {
        return 'Say "' + this.display_text(this.getParam('text')) + '"';
      } else if (this.type === 'wait') {
        return 'Wait ' + this.display_duration(this.getParam('duration')) + ' ' + this.getParam('time_period');
      }
    },

    display_location: function(loc) {
      if (loc) {
        return loc.name;
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

    // Return a javascript object that will be serialized as JSON and sent to the midtier
    toAPI: function() {
      var ret = {
        'name': this.type_to_API_mapping[this.type],
        'parameters': this.parameters
      };

      return ret;
    },
  });

  return Step;
});

