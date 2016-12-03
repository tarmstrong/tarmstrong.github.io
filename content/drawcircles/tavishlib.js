/*!
 * Tavish's ProcessingJS Library v0.0
 * http://tavisharmstrong.com/
 *
 * Copyright 2011, Tavish Armstrong
 * GPL Version 3 license.
 *
 */

(function (window, undefined) {

var Tavish = {};

Tavish.getRandomColor = function () {
  return [parseInt(Math.random()*255), parseInt(Math.random()*255), parseInt(Math.random()*255)];
};

Tavish.randint = function () {
  if (arguments.length === 1) {
    return parseInt(Math.random()*arguments[0]);
  } else if (arguments.length === 2) {
    return parseInt(Math.random()*(arguments[1] - arguments[0]));
  } else {
    throw "Invalid randint() arguments.";
  }
};

Tavish.randomBG = Tavish.randomBackground = function ($) {
  var color = Tavish.getRandomColor();
  $.background(color[0], color[1], color[2]);
};

Tavish.randomFill = Tavish.randomFG = function ($) {
  var color = Tavish.getRandomColor();
  $.fill(color[0], color[1], color[2]);
};

Tavish.randomStroke = function ($) {
  var color = Tavish.getRandomColor();
  $.stroke(color[0], color[1], color[2]);
};

window.Tavish = Tavish;

return Tavish;

})(window);
