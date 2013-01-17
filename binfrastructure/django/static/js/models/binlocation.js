var MyApp;
define([
  'ember',
  'emberdata',
  'app'
],
function( Ember, DS, App) {

  App.Binlocation = DS.Model.extend({
    name: DS.attr('string'),
    pose: DS.attr('string')
  });

  return App.Binlocation;
});

