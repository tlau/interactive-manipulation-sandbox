define([
  'ember',
  'app',
  'controllers/application',
  'views/application',
  'models/robot',
  'models/bin'
],
function(
  Ember,
  App,
  ApplicationController,
  ApplicationView,
  Robot,
  Bin
) {

  App.Router = Ember.Router.extend({
    root : Ember.Route.extend({
      index: Ember.Route.extend({
        route: '/',

        connectOutlets: function(router) {
        }
      }),
    })
  });
});

