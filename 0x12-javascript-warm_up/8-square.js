#!/usr/bin/node

let y = 0;

if (parseInt(process.argv[2])) {
  while (y < process.argv[2]) {
    console.log('X'.repeat(process.argv[2]));
    y += 1;
  }
} else {
  console.log('Missing size');
}
