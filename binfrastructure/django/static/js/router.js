define([
  'ember',
  'app',
  'controllers/application',
  'controllers/program',
  'views/application',
  'views/program',
  'models/robot',
  'models/bin'
],
function(
  Ember,
  App,
  ApplicationController,
  ProgramController,
  ApplicationView,
  ProgramView,
  Robot,
  Bin
) {

  App.Router = Ember.Router.extend({
    root : Ember.Route.extend({
      index: Ember.Route.extend({
        route: '/',

        connectOutlets: function(router) {
          router.get('applicationController').connectOutlet('program', 'program');
        }
      }),
    })
  });
});

