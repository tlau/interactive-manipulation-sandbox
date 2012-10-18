define([
    'ember',
    'app',
    'd3',
    'text!templates/map.handlebars'
],function(Ember,App,d3,mapHtml) {

  App.MapView = Ember.View.extend({
    template: Ember.Handlebars.compile(mapHtml),
    didInsertElement: function() {
      var w = 480,
        h = 374,
        x = d3.scale.linear().domain([0, w]),
        y = d3.scale.ordinal().domain([0, h]);

        var svg = d3.select("#floorplan-div").append("svg")
          .attr("width", w)
          .attr("height", h)
          .attr("id","mapsvg");

        svg.append("svg:image")
          .attr("xlink:href", "/static/images/willow-floorplan.png")
          .attr("width", w)
          .attr("height", h);

      // Observer so that when the places in the database change, we update
      // the map
      var content = this.get('controller').get('content');
      var places = content.places;
      places.addArrayObserver(this);

      // Add an observer so that whenever the robot's position changes, we
      // update the map
      var robot = content.robot;
      robot.addObserver('map_coords', this, 'drawRooms');
    },

    arrayWillChange: function() {},
    arrayDidChange: function() {
      this.drawRooms();
    },

    drawRooms: function() {
      var content = this.get('controller').get('content');
      var robot = content.robot;
      var places = content.places.toArray();

      // Draw each room and outlet on the map
      this.drawPlaces(places);

      // Plot the robot on the map last, so that it comes out on top
      this.drawRobot(robot);

      // Figure out which room the robot is closest to
      var nearest = -1;
      var closest_place = null;
      for (var i=0; i<places.length; i++) {
        var place = places[i];
        if (place.get('map_x') === null || place.get('map_y') === null) continue;
        var robot_coords = robot.get('map_coords');

        // First check if the robot is inside
        var map_x = place.get('map_x');
        var map_y = place.get('map_y');
        var height = place.get('map_height');
        var width = place.get('map_width');
        var rx = robot_coords.x;
        var ry = robot_coords.y;
        if ((map_x - 1 <= rx) &&
          (rx <= (map_x + width + 1)) &&
          (map_y - 1 <= ry) &&
          (ry <= (map_y + height + 1))) {
            closest_place = place;
            break;
        }

        // Otherwise, find its distance to the nearest corner of the room
        var distance = this.getDistance(robot_coords, place);
        if ((nearest == -1) || distance < nearest) {
          nearest = distance;
          closest_place = place;
        }
      }
      if (closest_place != null) {
        d3.select("#closest").text(closest_place.get('name'));
      }
    },

    getDistance : function(robot, place) {
      var rx = robot.x;
      var ry = robot.y;
      var px = place.get('map_x');
      var py = place.get('map_y');
      var h = place.get('map_height');
      var w = place.get('map_width');
      return Math.sqrt(Math.min(
        Math.pow(rx - px, 2) + Math.pow(ry - py, 2),
        Math.pow(rx - (px+h), 2) + Math.pow(ry - py, 2),
        Math.pow(rx - (px), 2) + Math.pow(ry - py+h, 2),
        Math.pow(rx - (px+h), 2) + Math.pow(ry - py+h, 2)));
    },

    drawRobot: function(robot) {
      var map = d3.select("#mapsvg");
      var _this = this;

      if ((robot.get('map_coords').x == -1) || (robot.get('map_coords').y == -1)) {
        return;
      }

      /* Draw our robet on the map */
      map.selectAll(".robot")
        .data([robot])
        .enter().append("svg:circle")
          .attr("class", "robot")
          .attr("cx", function(d) {
              return d.get('map_coords').x;
            })
          .attr("cy", function(d) {
              return d.get('map_coords').y;
            })
          .attr("r", 5);
    },

    drawPlaces: function(places) {
      if (!places) {
        return;
      }

      var rooms = places.filter( function(p) { return !p.get('isOutlet'); });
      var outlets = places.filter( function(p) { return p.get('isOutlet'); });
      var map = d3.select("#mapsvg");

      /* When the user clicks on a room, update "Selected location" and
       * store this place name in our controller */
      function nodeSelected(d) {
        // Remove old selection
        d3.select(".selected").classed("selected", false);
        // Add new selection
        d3.select(d3.event.target).classed("selected", true);

        // Populate the "Selected location" text field
        d3.select("#placename").text(d.get('name'));
        // Store this place id in our controller
        _this.get('controller').set('placeId', d.get('id'));
      }

      /* Draw Rooms */
      var _this = this;
      map.selectAll(".room")
        .data(rooms.toArray())
        .enter().append("svg:rect")
          .attr("class", "room")
          .attr("x", function(d) { return d.get('map_x'); })
          .attr("y", function(d) { return d.get('map_y'); })
          .attr("width", function(d) { return d.get('map_width'); })
          .attr("height", function(d) { return d.get('map_height'); })
          .on("click", nodeSelected);

      /* Draw Outlets */
      map.selectAll(".outlet")
        .data(outlets.toArray())
        .enter().append("svg:image")
          .attr("class", "outlet")
          .attr("xlink:href", "/static/outlet.jpg")
          .attr("x", function(d) { return d.get('map_x'); })
          .attr("y", function(d) { return d.get('map_y'); })
          .attr("width", 20)
          .attr("height", 20)
          .on("click", nodeSelected);
    }
  });

});
