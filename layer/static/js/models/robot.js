define([
  'ember',
  'emberdata',
  'app',
  'ros',
  'action',
],
function( Ember, DS, App, ros, Action) {

  App.Robot = DS.Model.extend({
    name: DS.attr('string'),
    description: DS.attr('string'),
    tags: DS.attr('string'),
    image: DS.attr('string'),
    state: DS.attr('number'),
    service_url: DS.attr('string'),
    camera_url: DS.attr('string'),
    forearm_camera_url: DS.attr('string'),
    battery: -1,
    plugged_in_value: -1,
    pose: { 'x': -1 , 'y': -1 },
    plugged_in: function() {
      return (this.get('plugged_in_value') > 0);
    }.property('plugged_in_value'),

    map_coords: function() {
      var pose = this.get('pose');
      var map_x, map_y;
      if (pose.x == -1) {
        map_x = -1;
      } else {
        map_x = -3.2371041 * pose.x + -7.70845759 * pose.y + 564.53259318;
      }
      if (pose.y == -1) {
        map_y = -1;
      } else {
        map_y = -7.90508822 * pose.x + 3.38653133 * pose.y + 295.37609582;
      }
      return {'x': map_x, 'y': map_y};
    }.property('pose'),

    serviceUrlChanged: function() {
      if(this.get('service_url')) {
        ros.connect(this.get('service_url'));
        var topic = new ros.Topic({
          name: '/dashboard_agg',
          messageType: 'pr2_msgs/DashboardState'
        });
        var _this = this;
        topic.subscribe(function(message) {
          _this.set('battery', message.power_state.relative_capacity);
          _this.set('plugged_in_value', message.power_state.AC_present);
        });

        // Also subscribe to robot location changes
        var loc_topic = new ros.Topic({
          name: '/robot_pose',
          messageType: 'geometry_msgs/PoseWithCovarianceStamped'
        });
        var _this = this;
        loc_topic.subscribe(function(message) {
          _this.set('pose', {
            'x' : message.pose.pose.position.x,
            'y' : message.pose.pose.position.y
            });
        });
      }
    }.observes('service_url'),

    navigateTo: function(place) {
      var action = new Action({
        ros: ros,
        name: 'NavigateToPose'
      });
      action.inputs.x        = place.get('pose_x');
      action.inputs.y        = place.get('pose_y');
      action.inputs.theta    = place.get('pose_angle');
      action.inputs.frame_id = '/map';
      action.execute();
      console.log('Calling NavigateTo action');
    },

    unplug: function() {
      var action = new Action({
        ros: ros,
        name: 'Unplug'
      });
      action.execute();
      console.log("Calling Unplug action");
    },

    plugIn: function() {
      var action = new Action({
        ros: ros,
        name: 'PlugIn'
      });
      action.execute();
      console.log("Calling PlugIn action");
    }
  });
});

