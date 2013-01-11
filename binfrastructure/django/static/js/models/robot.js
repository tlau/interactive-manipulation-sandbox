var MyApp;
define([
  'ember',
  'emberdata',
  'app'
],
function( Ember, DS, App) {
  MyApp = App;

  App.Robot = DS.Model.extend({
    id: DS.attr('string'),
    location_x: DS.attr('number'),
    location_y: DS.attr('number'),
    is_holding_bin: DS.attr('boolean')
  });
});

