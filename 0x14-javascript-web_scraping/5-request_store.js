#!/usr/bin/node
/*
 *script that writes a string to a file.
 */
const fs = require('fs');
const request = require('request');
const rUrl = process.argv[2];
request(rUrl, function (err, res, body) {
  if (err) {
    return console.log('Error: ', err);
  } else if (res.statusCode === 200) {
    fs.writeFile(process.argv[3], body, function (err) {
      if (err) {
        return console.log(err);
      }
    });
  }
});
