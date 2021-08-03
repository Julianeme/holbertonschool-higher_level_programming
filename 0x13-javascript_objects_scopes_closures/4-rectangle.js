#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    /* Prints the rectangle */
    let high = 0;
    while (high < this.height) {
      console.log('X'.repeat(this.width));
      high += 1;
    }
  }

  rotate () {
    /* exchanges the width and the height of the rectangle */
    const tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }

  double () {
    /* multiples the width and the height of the rectangle by 2 */
    this.width *= 2;
    this.height *= 2;
  }
};
