requirejs.config({
  enforceDefine: true,
  waitSeconds: 300,

  paths: {
    jquery       : 'libs/jquery',
    d3           : 'libs/d3',
    blockUI      : 'libs/jquery.blockUI',
    // socket.io
    io           : 'libs/socket.io',
    // Ember
    handlebars   : 'libs/handlebars',
    ember        : 'libs/ember',
    emberdata    : 'libs/ember-data',
    // Require.js Plugins
    text         : 'libs/text',
    // Templates
    templates     : '../templates'
  },

  shim: {
    'd3': {
      exports: 'd3'
    },
    'handlebars': {
      exports: 'Handlebars'
    },
    'ember': {
      deps    : ['jquery', 'blockUI', 'handlebars'],
      exports : 'Ember'
    },
    'emberdata': {
      deps    : ['jquery', 'ember'],
      exports : 'DS'
    }
  }
});

define([
  'app',
  'monitor/router',
  'jquery'
],
function(App, Router, $) {
  $('.loading').remove();
  App.initialize();
});
