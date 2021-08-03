#!/usr/bin/node
/* returns the reversed version of a list */

exports.esrever = function (list) {
  const tempList = [];
  let index = list.length - 1;
  while (index >= 0) {
    tempList.push(list[index]);
    index -= 1;
  }
  return tempList;
};
