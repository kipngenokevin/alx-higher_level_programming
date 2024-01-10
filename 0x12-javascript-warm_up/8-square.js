#!/usr/bin/node
const arg1 = parseInt(process.argv[2]);
if (arg1) {
  for (let i = 0; i < arg1; i++) {
    console.log('X'.repeat(arg1));
  }
} else {
  console.log('Missing size');
}
