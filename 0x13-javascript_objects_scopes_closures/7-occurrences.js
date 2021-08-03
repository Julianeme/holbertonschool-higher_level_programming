#!/usr/bin/node
/* returns the number of occurrences in a list */

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (const element of list) {
    if (element === searchElement) {
      counter += 1;
    }
  }
  return counter;
};
