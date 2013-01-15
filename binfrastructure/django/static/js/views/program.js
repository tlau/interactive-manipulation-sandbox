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

    program: new Array('step one', 'step two'),

    didInsertElement: function() {
      console.log("in didIE for Program");

//      var controller = this.get('controller');
//      console.log('setting observer on', controller);
//      controller.addObserver('program', this, 'drawProgram');

      this.drawProgram();
    },

    drawProgram: function() {

      var _this = this;
      var stepdiv = d3.select('.step_container');
      var steps = stepdiv.selectAll('.step')
        .data(this.program);

      steps.enter().append('div')
          .attr('class', 'step nonselectable');

      steps
          .attr('index', function(d, i) { return i; })
          .text(function(d) { return d; })
          .append('span')
            .attr('class', 'deletebutton nonselectable')
            .text('[X]')
            .on('click', function(d, i) { _this.deleteStep(i); });

        steps.exit().remove();
    },

    deleteStep: function(index) {
      this.program.splice(index, 1);
      this.drawProgram();
    },

    addStep: function(newstep) {
      this.program.push(newstep);

      // manually redraw the program as a workaround; why dosen't the observer work?
      this.drawProgram();
    },
  
    pickup : function(evt) {
      this.addStep('Pick up from the kitchen');
    },

    dropoff: function(evt) {
      this.addStep('Drop off at Elvio\'s office');
    },

    speak: function(evt) {
      this.addStep('Say "Hello!"');
    },

    wait: function(evt) {
      this.addStep('Wait 30 seconds');
    },

    recharge: function(evt) {
      this.addStep('Recharge batteries');
    }

  });

});


