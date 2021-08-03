#!/usr/bin/node
/* class Square that defines a square and inherits from Rectangle of 4-rectangle.js */

const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let side = 0;
    let pattern = 'C';
    if (c !== 'c' && c !== 'C') {
      pattern = 'X';
    } while (side < this.width) {
      console.log(pattern.repeat(this.width));
      side += 1;
    }
  }
};
