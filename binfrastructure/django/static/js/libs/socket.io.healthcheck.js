define([
  'socketio'
],
function(
  io
) {

  /**
   * The health check namespace.
   *
   * @api public.
   */

  var HealthCheck = {};

  /**
   * Configuration affecting all extended sockets.
   *
   * @api private.
   */

  HealthCheck.config = {
    interval: 2000,   // milliseconds between health checks.
    averageLength: 10 // number of values to compute running averages on.
  };

  /**
   * Data shared by all extended sockets.
   *
   * @api private.
   */

  HealthCheck.data = {
  };

  /**
   * RTT computing algorithm.
   *
   * @param [healthCheckData] reference health check related data object.
   * @param {Number} [delta] Milliseconds for the current RTT measured.
   * @api private
   */

  HealthCheck.computeRTT = function(healthCheckData, delta){
    healthCheckData.rtt = delta;
  };


  /**
   * Algorithm to approximate latency.
   *
   * Use a running average of the computed round trip time to approximate latency.
   *
   * @param [healthCheckData] reference health check related data object.
   * @api private
   */

  HealthCheck.computeLatency = function(healthCheckData){
    var latency = 0;

    // Use the data object to store previous delta values.
    healthCheckData.RTTs = healthCheckData.RTTs || [];

    // Push current value with the old ones.
    if (healthCheckData.RTTs.length === HealthCheck.config.averageLength){
      // Buffer of old values is full, loose the oldest.
      healthCheckData.RTTs = healthCheckData.RTTs.slice(1);
    }
    healthCheckData.RTTs.push(healthCheckData.rtt);

    // Compute the running average to approximate the latency.
    for (var a = healthCheckData.RTTs, l = a.length, i = 0; i < l; i++){
      latency += a[i];
    }
    latency = latency / healthCheckData.RTTs.length;

    healthCheckData.latency = latency;
  };

  /**
   * Update health data for a single socket.
   *
   * @api private
   */

  HealthCheck.update = function(healthCheckData, delta){
    // Compute round trip time.
    HealthCheck.computeRTT(healthCheckData, delta);

    // Using the values computed, approximate latency.
    HealthCheck.computeLatency(healthCheckData);
  };

  HealthCheck.resetData = function(socket){
    socket.healthCheck = {
      data: {
        latency: 0,
        rtt: 0
      }
    };
  };

  /**
   * Extend a connected socket to provide connection health information.
   *
   * For now, provide the functionality as a function to extend an SocketNamespace object.
   *
   * The callback passed will receive as only argument the health check data object.
   *
   * @param {io.SocketNamespace} [socket] the socket object to extend.
   * @param {Function} [onHealthCheck] Called back upon a health check update.
   * @returns {io.SocketNamespace}
   * @api public
   */
  HealthCheck.extend = function(socket, onHealthCheck){

    // Connection health related data exclusive to this sockets.
    HealthCheck.resetData(socket);

    // Forget old values upon disconnect.
    socket.on('disconnect', function(){ HealthCheck.resetData(socket)});

    socket.on('connect', function(){
      // Initiate the health check routine, sending the first health check packet.
      socket.emit('health check', {latency: 0, timestamp: (new Date).getTime()});
    });

    // Handle server responses to health checks.
    socket.on('health check', function(healthCheckPacket){
      // Immediately compute the time delta.
      var delta = (new Date).getTime() - healthCheckPacket.timestamp;

      HealthCheck.update(socket.healthCheck.data, delta);

      // Expose the health data to the application.
      var healthCheckData = {
        rtt: socket.healthCheck.data.rtt,
        latency: socket.healthCheck.data.latency
      };
      onHealthCheck(healthCheckData);
    });

    // Send health checks to the server at intervals.
    socket.healthCheck._interval = setInterval(function(){
      // Expose the health data to the server.
      var healthCheckData = {
        latency: socket.healthCheck.data.latency,
        timestamp: (new Date).getTime()
      };
      socket.emit('health check', healthCheckData);
    }, HealthCheck.config.interval);

    // Return the extended socket object.
    return socket;
  };

  return HealthCheck;
});
