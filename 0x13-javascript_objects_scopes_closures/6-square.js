#!/usr/bin/node
/* class Square that defines a square and inherits from Rectangle of 4-rectangle.js */

const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let side = 0;
    this.pattern = c;
    if (!this.pattern) {
      this.pattern = 'X';
    } while (side < this.width) {
      console.log(this.pattern.repeat(this.width));
      side += 1;
    }
  }
};
