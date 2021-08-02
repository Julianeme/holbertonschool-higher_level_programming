#!/usr/bin/node

const args = process.argv;
let biggest = process.argv[2];
let secondBiggest = process.argv[2];
if (args.length > 3) {
  for (let i = 2; i < args.lenght; i++) {
    if (biggest > args[i]) {
      biggest = args[i];
    }
  } for (let j = 2; j < args.lenght; j++) {
    if (secondBiggest > args[j] && secondBiggest < biggest) {
      secondBiggest = args[j];
    }
  }
} else {
  secondBiggest = 0;
}
console.log(secondBiggest);
