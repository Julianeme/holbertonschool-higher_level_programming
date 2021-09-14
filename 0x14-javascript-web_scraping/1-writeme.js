#!/usr/bin/node
/*
 *script that reads and prints the content of a file.
 */
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], function (err) {
  if (err) {
    return console.log(err);
  }
});
