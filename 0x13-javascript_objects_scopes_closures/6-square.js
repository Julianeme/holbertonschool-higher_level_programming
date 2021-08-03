#!/usr/bin/node
/* class Square that defines a square and inherits from Rectangle of 4-rectangle.js */

module.exports = class Square extends require('./5-rectangle') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let side = 0;
    if (!c) {
      c = 'X';
    } while (side < this.width) {
      console.log(c.repeat(this.width));
      side += 1;
    }
  }
};
