define([
  'ember',
  'd3',
  'app',
  'step',
  'models/binlocation',
  'text!templates/program.handlebars'
],
function(
  Ember,
  d3,
  App,
  Step,
  Binlocation,
  programHtml
) {

  App.ProgramView = Ember.View.extend({
    template: Ember.Handlebars.compile(programHtml),

    // Keeping track of the program and the program counter
    program: new Array(),
    selected_step: null,

    // Soon this will be loaded from the database instead
    locations: Binlocation.find(),
    /*
    [
      { 'name': "Elvio's office" },
      { 'name': "Julian's office" },
      { 'name': "the kitchen" },
      { 'name': "the Green Room" },
      { 'name': "the stockroom" },
      { 'name': "Esmi's office" },
      { 'name': "Kaijen's office" },
      { 'name': "the White Lab" }
    ],
    */
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
      var _this = this;
      var stepdiv = d3.select('.step_container');
      var steps = stepdiv.selectAll('.step')
        .data(this.get('program'));

      steps.enter().append('div')
          .attr('class', 'step nonselectable')
          .on('click', function(d, i) { _this.selectStep(i); });

      steps
          .attr('index', function(d, i) { return i; })
          .text(function(d) { return d.display_title(); })
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

      if (step.getParam('pose')) {
        this.set('map_xy', this.transformPoseToMap(step.getParam('pose')));
        console.log('map_xy is:', this.get('map_xy'));
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
      this.set('map_xy', null);
    },

    /* ---------------------------------------------------------------------- */
    // Specific actions

    /* PICKUP ---------------------------------------------------------------------- */
    pickup: function(evt) {
      this.addStep(Step.create({
        'type': 'pickup'
        }));
    },

    onLocationChange: function(evt) {
      if (!this.get('selected_location')) return;

      var step = this.get('program')[this.get('selected_step')];
      if (step) {
        step.setParam('location', this.get('selected_location'));
      } else {
        console.log("Error: setting parameter of unknown step!");
      }

      // Refresh the program
      this.drawProgram();
    }.observes('selected_location'),

    /* DROPOFF ---------------------------------------------------------------------- */
    dropoff: function(evt) {
      this.addStep(Step.create({
        'type': 'dropoff'
        }));
    },

    /* GOTO ---------------------------------------------------------------------- */
    gotoPlace: function(evt) {
      this.addStep(Step.create({
        'type': 'goto'
        }));
    },

    onSelectLocation: function(evt) {
      // Workaround for Firefox because it does not provide the offsetX/Y values
      if (typeof evt.offsetX === 'undefined' || typeof evt.offsetY === 'undefined') {
        var targetOffset = $(evt.target).offset();
        evt.offsetX = evt.pageX - targetOffset.left;
        evt.offsetY = evt.pageY - targetOffset.top;
      }

      this.set('map_xy', {x: evt.offsetX, y: evt.offsetY});

      // Update Pose in selected step
      var step = this.get('program')[this.get('selected_step')];
      if (step) {
        step.setParam('pose', this.transformMapToPose(this.get('map_xy')));
      } else {
        console.log("Error: setting parameter pose of unknown step!");
      }

      this.drawProgram();
    },

    drawSelectedPointOnMap: function() {
      console.log("drawing selected point on map");
      if (this.get('map_xy') === null) return;

      var _this = this;
      var map = d3.select('#map');
      var mappoint = map.selectAll('.mappoint')
        .data([this.get('map_xy')]);

      mappoint.enter().append('svg:circle')
        .attr('class', 'mappoint')
        .attr('r', 5);

      mappoint
        .attr('cx', function(d) {return d.x;})
        .attr('cy', function(d) {return d.y;});

      mappoint.exit().remove();
    }.observes('map_xy'),

    /* SPEAK ---------------------------------------------------------------------- */
    speak: function(evt) {
      this.addStep(Step.create({
        'type': 'speak'
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

    /* WAIT ---------------------------------------------------------------------- */
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
      };

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
      var program = {name: ''},
          brick = '';

      program.name = ''; // Inmediate execution of an anonymous program.
      program.steps = this.get('program').map(function (d) { return d.toAPI(); });
      // Compile the pretty flower into an ugly brick.
      brick = JSON.stringify(program);

      // Send the brick to the middleware layer here
      console.log(brick);
      var xhr = new XMLHttpRequest();
      xhr.open('POST', '/world/api/run/program', true);
      xhr.setRequestHeader('Content-type', 'application/json');
      xhr.onreadystatechange = function() {
        // Call this when the state changes
        if (xhr.readyState == 4 && xhr.status == 200) {
          console.log("Server response:", xhr.responseText);
          if (xhr.responseText) {
            alert(xhr.responseText);
          } else {
            alert("Program appears to have run ok...");
          }
        }
      };
      xhr.send(brick);
    },

    saveProgram: function(evt) {

      var steps = this.get('program').map(function (d) { return d.toAPI(); });
      var ret = {
        'steps': steps,
        'name': 'My Program'
      };
      var ret_json = JSON.stringify(ret);
      console.log(ret_json);

      // Send ret to the middleware layer here
      var xhr = new XMLHttpRequest();
      xhr.open('POST', '/world/api/programs', true);
      xhr.setRequestHeader('Content-type', 'application/json')
      xhr.onreadystatechange = function() {
        // Call this when the state changes
        console.log("Server response:", xhr.responseText);
        if (xhr.readyState == 4 && xhr.status == 200) {
          console.log("Server response:", xhr.responseText);
        }
      };
      xhr.send(ret_json);
    },

    /* For converting map coords to a pose */
    transformMapToPose: function(map) {
      var pose = {};
      if (map.x === -1) {
        pose.x = -1;
      }
      else {
        pose.x = -0.0471014974 * map.x + -0.107212915 * map.y + 58.2584626;
      }
      if (map.y === -1) {
        pose.y = -1;
      }
      else {
        pose.y = -0.109947748 * map.x + 0.045023192 * map.y + 48.7703124;
      }
      return pose;
    },

    /* For converting a pose to map coordinates */
    transformPoseToMap: function(pose) {
      var map = {};
      if (pose.x === -1) {
        map.x = -1;
      }
      else {
        map.x = -3.2371041 * pose.x + -7.70845759 * pose.y + 564.53259318;
      }
      if (pose.y === -1) {
        map.y = -1;
      }
      else {
        map.y = -7.90508822 * pose.x + 3.38653133 * pose.y + 295.37609582;
      }
      return map;
    }

  });

});
