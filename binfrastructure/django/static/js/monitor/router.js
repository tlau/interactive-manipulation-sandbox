define([
  'ember',
  'app',
  'io',
  'controllers/application',
  'controllers/monitor',
  'views/application',
  'views/monitor',
  'models/robot',
  'models/bin',
  'models/binlocation'
],
function(
  Ember,
  App,
  io,
  ApplicationController,
  MonitorController,
  ApplicationView,
  MonitorView,
  Robot,
  Bin,
  Binlocation
) {

  App.Router = Ember.Router.extend({
    root : Ember.Route.extend({
      index: Ember.Route.extend({
        route: '/',

        connectOutlets: function(router) {
          router.get('applicationController').connectOutlet('program', 'monitor');
        }
      }),
    })
  });
});

