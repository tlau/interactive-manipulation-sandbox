define([
  'ember',
  'app',
  'io'
],
function(
  Ember,
  App,
  io
) {

  App.MonitorController = Ember.Controller.extend({
    on_step: function( data) {
      console.log('New step event received from CPU: ' + data);
      //  HERE: Do something useful with this event
    },





    init: function() {
      console.log('init');
      this._super();
      this.socket = io.connect('/cpu');
      this.map_event('step');
    },

    //  This is a convenience function that should be abstracted away
    //  in a library class or something. Perhaps there are known ways
    //  of doing this with socket.io or eventemitter and all
    map_event: function(eventName) {
      var _this = this;
      this.socket.on(eventName, function( data) {
        _this['on_'+eventName]( data);
      });
    }
  });

  return App.MonitorController;
});

