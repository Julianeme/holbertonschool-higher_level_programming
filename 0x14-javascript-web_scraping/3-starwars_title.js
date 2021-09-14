#!/usr/bin/node
/*
 *script that writes a string to a file.
 */
const request = require('request');
const rUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(rUrl, function (err, res, body) {
  if (err) {
    return console.log('Error: ', err);
  } else if (res.statusCode === 200) {
    const chars = JSON.parse(body).title;
    for (character of chars){
      console.log("character is: %s", character)}
  }
});
