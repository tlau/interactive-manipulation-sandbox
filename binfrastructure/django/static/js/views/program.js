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

    // Keeping track of the program and the program counter
    program: new Array(),
    selected_step: null,

    // Soon this will be loaded from the database instead
    locations: [
      { 'name': "Elvio's office" },
      { 'name': "Julian's office" },
      { 'name': "the kitchen" },
      { 'name': "the Green Room" },
      { 'name': "the stockroom" },
      { 'name': "Esmi's office" },
      { 'name': "Kaijen's office" },
      { 'name': "the White Lab" }
    ],
    selected_location: null,

    // Default time periods
    time_periods: [
      'seconds', 'minutes', 'hours'
    ],
    selected_time: null,

    didInsertElement: function() {
      // Doesn't work
      // this.addObserver('program', this, 'drawProgram');

      this.drawProgram();
    },

    drawProgram: function() {
      console.log("Drawing program", this.get('program'));
      var _this = this;
      var stepdiv = d3.select('.step_container');
      var steps = stepdiv.selectAll('.step')
        .data(this.get('program'));

      steps.enter().append('div')
          .attr('class', 'step nonselectable')
          .on('click', function(d, i) { _this.selectStep(i); });

      steps
          .attr('index', function(d, i) { return i; })
          .text(function(d) { console.log("getting step title for", d); return d.display_title(); })
          .attr('id', function(d, i) { return 'step' + i; })
          .append('span')
            .attr('class', 'deletebutton nonselectable')
            .text('[X]')
            .on('click', function(d, i) {
              _this.deleteStep(i);
              // Prevent the click from bubbling up to selectStep
              d3.event.stopPropagation();
            });

        steps.exit().remove();
    },

    /* ---------------------------------------------------------------------- */
    // Adding/deleting steps

    deleteStep: function(index) {
      // Remove the step from the program
      var program = this.get('program');
      program.splice(index, 1);
      this.set('program', program);

      // Update selected step
      if ((this.get('selected_step') < 0) || (this.get('selected_step') >= this.get('program').length)) {
        this.set('selected_step', null);
      } 

      // manually redraw the program; I can't get Ember observers to work
      this.drawProgram();
    },

    addStep: function(newstep) {
      var program = this.get('program');
      var index = program.push(newstep) - 1;
      this.set('program', program);

      // manually redraw the program; I can't get Ember observers to work
      this.drawProgram();
      this.selectStep(index);
    },

    // Change which step is currently selected
    selectStep: function(index) {
      this.set('selected_step', index);

      $('.selected').removeClass('selected');
      $('#step' + index).addClass('selected');

      var step = this.get('program')[index];
      this.showPanel(step.type);

      // Wiring to update UI which Ember would have done for us
      if (step.getParam('location')) {
        this.set('selected_location', step.getParam('location'));
      }

      if (step.getParam('duration')) {
        this.set('selected_time', step.getParam('duration'));
      }
      if (step.getParam('time_period')) {
        this.set('selected_time_period', step.getParam('time_period'));
      }

      if (step.getParam('text')) {
        this.set('text_to_speak', step.getParam('text'));
      }
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
      this.set('selected_location', null);
      this.set('selected_time', null);
      this.set('selected_time_period', null);
      this.set('text_to_speak', null);
    },
  
    /* ---------------------------------------------------------------------- */
    // Specific actions

    pickup : function(evt) {
      var loc = this.locations[Math.floor(Math.random() * this.locations.length)].name;
      this.addStep(Step.create({
        'type': 'pickup'
        }));
    },

    onLocationChange: function(evt) {
      if (!this.get('selected_location')) return;

      console.log('selected location:', this.get('selected_location').name); 
      var step = this.get('program')[this.get('selected_step')];
      if (step) {
        step.setParam('location', this.get('selected_location'));
      } else {
        console.log("Error: setting parameter of unknown step!");
      }

      // Refresh the program
      this.drawProgram();
    }.observes('selected_location'),

    dropoff: function(evt) {
      var loc = this.locations[Math.floor(Math.random() * this.locations.length)].name;
      this.addStep(Step.create({
        'title': 'Drop off at ' + loc,
        'type': 'dropoff',
        'location': loc,
        }));
    },

    gotoPlace: function(evt) {
      var loc = this.locations[Math.floor(Math.random() * this.locations.length)].name;
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

    onSpeakTextChange: function(evt) {
      if (this.get('text_to_speak')) {
        var step = this.get('program')[this.get('selected_step')];
        if (step) {
          step.setParam('text', this.get('text_to_speak'));
        } else {
          console.log("Error: setting parameter of unknown step!");
        }
      }

      // Refresh the program
      this.drawProgram();
    }.observes('text_to_speak'),

    wait: function(evt) {
      var num = (Math.floor(Math.random() * 29) + 1) * 10;
      var step = Step.create({
        'type':'wait',
        });
      step.setParam('time_period', 'seconds');
      this.addStep(step);
    },

    onTimeChange: function(evt) {
      if (this.get('selected_time')) {
        var step = this.get('program')[this.get('selected_step')];
        if (step) {
          step.setParam('duration', this.get('selected_time'));
        } else {
          console.log("Error: setting parameter of unknown step!");
        }
      }

      // Refresh the program
      this.drawProgram();
    }.observes('selected_time'),

    onTimePeriodChange: function(evt) {
      if (this.get('selected_time_period')) {
        var step = this.get('program')[this.get('selected_step')];
        if (step) {
          step.setParam('time_period', this.get('selected_time_period'));
        } else {
          console.log("Error: setting parameter of unknown step!");
        }
      }

      // Refresh the program
      this.drawProgram();
    }.observes('selected_time_period'),

    recharge: function(evt) {
      this.addStep(Step.create({
        'title': 'Dock with charger',
        'type':'recharge',
        }));
    },

    /* ---------------------------------------------------------------------- */
    // Program execution and saving
    runProgram: function(evt) {
      var ret = JSON.stringify(this.get('program').map(function (d) { return d.toAPI(); }));
      // Send ret to the middleware layer here
      console.log(ret);
      alert("Sorry, not implemented yet!");
    },

    saveProgram: function(evt) {
      
      var steps = this.get('program').map(function (d) { return d.toAPI(); });
      var ret = {
        'steps': steps,
        'name': 'My Program'
      };
      var ret_json = JSON.stringify(ret);

      // Send ret to the middleware layer here
      var xhr = new XMLHttpRequest();
      xhr.open('POST', '/world/api/programs', true);
      xhr.onreadystatechange = function() {
        // Call this when the state changes
        if (xhr.readyState == 4 && xhr.status == 200) {
          console.log(xhr.responseText);
        }
      };
      xhr.send(ret_json);
    },


  });

});
