#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const i = this.height;
    const j = this.width;
    this.height = j;
    this.width = i;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
