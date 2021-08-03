#!/usr/bin/node
/* creates a new list = initial value of the list * by its index */

const newList = require('./100-data.js').list;
console.log(newList);
console.log(newList.map((element, index) => element * index));
