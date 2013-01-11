define([
  'handlebars',
  'app'
],
function(Handlebars, App) {
  /* TL: This doesn't work. The parameter "arg" is called the literal
   * string name of the instance variable we want to render, not its value.
   */
  Handlebars.registerHelper('percent02f', function(arg) {
    return arg.toFixed(2);
  });
});
