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
    let high = 0;
    while (high < this.width) {
      console.log('X'.repeat(this.height));
      high += 1;
    }
  }

  double () {
    /* multiples the width and the height of the rectangle by 2 */
    let high = 0;
    while (high < (2 * this.height)) {
      console.log('X'.repeat((2 * this.width)));
      high += 1;
    }
  }
};
