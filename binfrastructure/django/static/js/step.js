define([
  'ember',
  'app',
  'models/binlocation',
  'jquery'
],
function(
  Ember,
  App,
  Binlocation,
  $
) {

  var Step = Ember.Object.extend({
    type: null,

    // We have to initialize the parameters array inside of the constructor otherwise
    // all Step instances will share the same copy of the parameters array
    init: function() {
      this._super();
      this.set('parameters', {});
    },

    setParam: function(name, value) {
      var newParams = $.extend({}, this.parameters);
      newParams[name] = value;
      this.set('parameters', newParams);
    },

    getParam: function(name) {
      return this.get('parameters')[name];
    },

    type_to_API_mapping: {
            'pickup': 'pick_up_bin_from_locations',
            'dropoff': 'drop_off_bin_at_locations',
            'goto': 'go_to_pose',
            'speak': 'speak',
            'wait': 'wait'
            },

    // Calculate a title property for this step derived from this step's type and parameters
    get_title: function() {
      var ret;
      if (this.type === 'pickup') {
        ret = 'Pick up from ' + this.display_location();
      } else if (this.type === 'dropoff') {
        ret = 'Drop off at ' + this.display_location();
      } else if (this.type === 'goto') {
        ret = 'Go to ' + this.display_pose(this.getParam('pose'));
      } else if (this.type === 'speak') {
        ret = 'Say "' + this.display_text(this.getParam('text')) + '"';
      } else if (this.type === 'wait') {
        ret = 'Wait ' + this.display_duration(this.getParam('duration')) + ' ' + this.getParam('time_period');
      }
//      console.log('### computed title:', ret);
      return ret;
    },

    display_location: function() {
      var ret = '???';
      var loc = this.getParam('location');
      if (loc) {
        if (loc.get('name')) {
          ret = loc.get('name');
        }
      }
      return ret;
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
      var ret = {
        'action': this.type_to_API_mapping[this.type],
        'params': this.parameters
      };

      return ret;
    },

    serialize: function() {
      var ret = {};
      ret.type = this.type;
      ret.params = {};
      if (this.parameters.location) {
        ret.params.location_id = this.parameters.location.id;
      }
      if (this.parameters.pose) {
        ret.params.pose = this.parameters.pose;
      }
      if (this.parameters.text) {
        ret.params.text = this.parameters.text;
      }
      if (this.parameters.duration) {
        ret.params.duration = this.parameters.duration;
      }
      if (this.parameters.time_period) {
        ret.params.time_period = this.parameters.time_period;
      }
      return ret;
    },

    deserialize: function(data) {
      this.type = data.type;
      var params = {};

      if (data.params.location_id) {
        params.location = Binlocation.find(data.params.location_id);
      }
      if (data.params.pose) {
        params.pose = data.params.pose;
      }
      if (data.params.text) {
        params.text = data.params.text;
      }
      if (data.params.duration) {
        params.duration = data.params.duration;
      }
      if (data.params.time_period) {
        params.time_period = data.params.time_period;
      }

      this.set('parameters', params);
    }
  });

  return Step;
});

