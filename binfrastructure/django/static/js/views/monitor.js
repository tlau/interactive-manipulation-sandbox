define([
  'ember',
  'app',
  'text!templates/monitor.handlebars'
],
function(
  Ember,
  App,
  html
) {

  App.MonitorView = Ember.View.extend({
    template: Ember.Handlebars.compile(html)
  });

});


