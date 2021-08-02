#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  for (let rept = 0; rept < x; rept++) {
    theFunction();
  }
};
