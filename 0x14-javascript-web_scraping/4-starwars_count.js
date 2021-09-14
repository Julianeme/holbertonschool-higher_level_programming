#!/usr/bin/node
/*
*script that writes a string to a file.
*/
const request = require('request');
const rUrl = process.argv[2];
let starredMovies = 0;
request(rUrl, function (err, res, body) {
  if (err) {
    return console.log('Error: ', err);
  } else if (res.statusCode === 200) {
    res = JSON.parse(body).results;
    for (const movies of res) {
      const charList = movies.characters;
      for (const stars of charList) {
        if (stars.endsWith('18/') === true) {
          starredMovies = starredMovies + 1;
        }
      }
    }
    console.log(starredMovies);
  }
});
