var MyApp;
define([
  'ember',
  'emberdata',
  'app'
],
function( Ember, DS, App) {

  App.Bin = DS.Model.extend({
    id: DS.attr('string'),
    location_x: DS.attr('number'),
    location_y: DS.attr('number'),
    tags: DS.attr('string')
  });
});

