#!/usr/bin/node
/*
 *script that writes a string to a file.
 */
const request = require('request');
request(process.argv[2], function (err, res) {
  if (err) return console.log('Error: ', err);
  console.log('code: %d', res.statusCode);
});
