#!/usr/bin/node
/*
 *script that writes a string to a file.
 */
const request = require('request');
const r_url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2]
request(r_url, function (err, res, body) {
  if (err) {return console.log('Error: ', err);
  } else if (JSON.parse(body).episode_id == process.argv[2]) {

    console.log('Episodio: %s', JSON.parse(body).title);
  }
});
