define([
  'ember',
  'd3',
  'app',
  'step',
  'text!templates/program.handlebars'
],
function(
  Ember,
  d3,
  App,
  Step,
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
      var index = this.program.push(newstep) - 1;

      // manually redraw the program; I can't get Ember observers to work
      this.drawProgram();
      this.selectStep(index);
    },

    // Change which step is currently selected
    selectStep: function(index) {
      $('.selected').removeClass('selected');
      $('#step' + index).addClass('selected');

      var step = this.program[index];
      this.showPanel(step.type);
    },

    showPanel: function(steptype) {
      // Change the right panel to display step parameters
      if (steptype === null) {
        // Show the actions panel
        $('.selectedPanel').addClass('hidden');
        $('.selectedPanel').removeClass('selectedPanel');
        $('#actions').removeClass('hidden');
      } else {
        // Hide the actions panel and the current step panel (if any)
        $('#actions').addClass('hidden');
        $('.selectedPanel').addClass('hidden');
        $('#' + steptype).removeClass('hidden');
        $('#' + steptype).addClass('selectedPanel');
      }
    },

    // Switch back to actions view
    doneEditingStep: function(index) {
      this.showPanel(null);
    },
  
    /* ---------------------------------------------------------------------- */
    // Specific actions

    pickup : function(evt) {
      var locations = new Array("Elvio's office", "Julian's office", "the kitchen",
        "the Green Room", "the stockroom", "Esmi's office", "Kaijen's office", "the White Lab");
      var loc = locations[Math.floor(Math.random() * locations.length)];
      this.addStep(Step.create({
        'title': 'Pick up from ' + loc,
        'type': 'pickup',
        'location': loc,
        }));
    },

    dropoff: function(evt) {
      var locations = new Array("Elvio's office", "Julian's office", "the kitchen",
        "the Green Room", "the stockroom", "Esmi's office", "Kaijen's office", "the White Lab");
      var loc = locations[Math.floor(Math.random() * locations.length)];
      this.addStep(Step.create({
        'title': 'Drop off at ' + loc,
        'type': 'dropoff',
        'location': loc,
        }));
    },

    gotoPlace: function(evt) {
      var locations = new Array("Elvio's office", "Julian's office", "the kitchen",
        "the Green Room", "the stockroom", "Esmi's office", "Kaijen's office", "the White Lab");
      var loc = locations[Math.floor(Math.random() * locations.length)];
      this.addStep(Step.create({
        'title': 'Take bin to ' + loc,
        'type': 'goto',
        'location': loc,
        }));
    },

    speak: function(evt) {
      this.addStep(Step.create({
        'title': 'Say "Hello!"',
        'type': 'speak',
        'text': 'Hello!',
        }));
    },

    wait: function(evt) {
      var num = (Math.floor(Math.random() * 29) + 1) * 10;
      this.addStep(Step.create({
        'title': 'Wait ' + num + ' seconds',
        'type':'wait',
        'duration': num,
        }));
    },

    recharge: function(evt) {
      this.addStep(Step.create({
        'title': 'Dock with charger',
        'type':'recharge',
        }));
    },

    /* ---------------------------------------------------------------------- */
    // Program execution
    runProgram: function(evt) {
      var ret = JSON.stringify(this.program.map(function (d) { return d.toAPI(); }));
      // Send ret to the middleware layer here
      console.log(ret);
      alert("Sorry, not implemented yet!");
    },



  });

});
