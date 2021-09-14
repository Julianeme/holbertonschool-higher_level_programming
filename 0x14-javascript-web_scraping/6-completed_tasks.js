#!/usr/bin/node
/*
*script that writes a string to a file.
*/
const request = require('request');
const rUrl = process.argv[2];
const tasksDict = {};
let key = 0;
request(rUrl, function (err, res, body) {
  if (err) {
    return console.log('Error: ', err);
  } else if (res.statusCode === 200) {
    for (const tasks of JSON.parse(body)) {
      if (tasks.completed === true) {
        key = tasks.userId;
        if (typeof tasksDict[key] === 'undefined') {
          tasksDict[key] = 0;
        }
        tasksDict[key] += 1;
      }
    }
    console.log(tasksDict);
  }
});
