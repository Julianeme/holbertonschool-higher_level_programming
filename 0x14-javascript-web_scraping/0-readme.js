#!/usr/bin/node

const fs = require('fs');
// __dirname means relative to script. Use "./data.txt" if you want it relative to execution path.
fs.readFile(process.argv[2], 'utf8', (error, data) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log(data);
});
