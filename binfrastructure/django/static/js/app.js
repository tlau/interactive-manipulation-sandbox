define([
  'ember',
  'emberdata',
  'jquery'
],
function(
  Ember,
  DS,
  $
) {
  var App = Ember.Application.create({
    autoinit: false,

    ready: function() {

    }

  });
  window.TheApp = App;

  /* Overriding behavior in RESTAdapter to handle responses of the type
      [{ object },{ object }, ...]
    as returned by default in django-rest-framework
    instead of currently required:
      { robots: [{ object },{ object }, ...]}

    NOTE: This can be greatly reduced in code size by generalizing the
    code that repeats between functions. I'm leaving it out for now
    to focus on the basics, but I should contribute this soon
  */
  DS.DjangoRESTAdapter = DS.RESTAdapter.extend({
    find: function( store, type, id) {
      var root = this.rootForType(type);
      this.ajax( this.buildURL(root, id), 'GET', {
        success: function( djson) {
          var json = {}; json[root] = djson;
          this.sideload(store, type, json, root);
          store.load(type, json[root]);
        }
      });
    },
    findMany: function( store, type, ids) {
      ids = this.get('serializer').serializeIds(ids);
      var root = this.rootForType(type), plural = this.pluralize(root);
      this.ajax( this.buildURL(root), 'GET', {
        data: { ids: ids },
        success: function( djson) {
          var json = {}; json[plural] = djson;
          this.sideload(store, type, json, plural);
          store.loadMany(type, json[plural]);
        }
      });
    },
    findAll: function( store, type) {
      var root = this.rootForType(type), plural = this.pluralize(root);
      this.ajax( this.buildURL(root), 'GET', {
        success: function( djson) {
          var json = {}; json[plural] = djson;
          this.sideload(store, type, json, plural);
          store.loadMany(type, json[plural]);
        }
      });
    },
    findQuery: function( store, type, query, recordArray) {
      var root = this.rootForType(type), plural = this.pluralize(root);
      this.ajax( this.buildURL(root), 'GET', {
        data: query,
        success: function(djson) {
          var json = {}; json[plural] = djson;
          this.sideload(store, type, json, plural);
          recordArray.load(json[plural]);
        }
      });
    }
  });

  App.store = DS.Store.create({
    revision: 6,
    adapter: DS.DjangoRESTAdapter.create({ namespace: 'world/api' })
  });

  return App;
});
