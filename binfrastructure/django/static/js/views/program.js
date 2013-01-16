define([
  'ember',
  'd3',
  'app',
  'text!templates/program.handlebars'
],
function(
  Ember,
  d3,
  App,
  programHtml
) {

  App.ProgramView = Ember.View.extend({
    template: Ember.Handlebars.compile(programHtml),

    program: new Array(),

    didInsertElement: function() {
      console.log("in didIE for Program");

      // Doesn't work
      // this.addObserver('program', this, 'drawProgram');

      this.drawProgram();
    },

    drawProgram: function() {
      var _this = this;
      var stepdiv = d3.select('.step_container');
      var steps = stepdiv.selectAll('.step')
        .data(this.program);

      steps.enter().append('div')
          .attr('class', 'step nonselectable')
          .on('click', function(d, i) { _this.selectStep(i); });

      steps
          .attr('index', function(d, i) { return i; })
          .text(function(d) { return d.title; })
          .attr('id', function(d, i) { return 'step' + i; })
          .append('span')
            .attr('class', 'deletebutton nonselectable')
            .text('[X]')
            .on('click', function(d, i) { _this.deleteStep(i); });

        steps.exit().remove();
    },

    /* ---------------------------------------------------------------------- */
    // Adding/deleting steps

    deleteStep: function(index) {
      this.program.splice(index, 1);
      // manually redraw the program; I can't get Ember observers to work
      this.drawProgram();
    },

    addStep: function(newstep) {
      this.program.push(newstep);

      // manually redraw the program; I can't get Ember observers to work
      this.drawProgram();
    },

    // Change which step is currently selected
    selectStep: function(index) {
      $('.selected').removeClass('selected');
      $('#step' + index).addClass('selected');
    },
  
    /* ---------------------------------------------------------------------- */
    // Specific actions

    pickup : function(evt) {
      var locations = new Array("Elvio's office", "Julian's office", "the kitchen",
        "the Green Room", "the stockroom", "Esmi's office", "Kaijen's office", "the White Lab");
      var loc = locations[Math.floor(Math.random() * locations.length)];
      this.addStep({
        'title': 'Pick up from ' + loc,
        });
    },

    dropoff: function(evt) {
      var locations = new Array("Elvio's office", "Julian's office", "the kitchen",
        "the Green Room", "the stockroom", "Esmi's office", "Kaijen's office", "the White Lab");
      var loc = locations[Math.floor(Math.random() * locations.length)];
      this.addStep({
        'title': 'Drop off at ' + loc,
        });
    },

    speak: function(evt) {
      this.addStep({
        'title': 'Say "Hello!"',
        });
    },

    wait: function(evt) {
      var num = (Math.floor(Math.random() * 29) + 1) * 10;
      this.addStep({
        'title': 'Wait ' + num + ' seconds',
        });
    },

    recharge: function(evt) {
      this.addStep({
        'title': 'Recharge batteries',
        });
    },

    /* ---------------------------------------------------------------------- */
    // Program execution
    runProgram: function(evt) {
      console.log("Run program pressed");
      alert("Not implemented yet!");
    }

  });

});


