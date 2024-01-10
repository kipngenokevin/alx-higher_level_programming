#!/usr/bin/node
const nArgs = parseInt(process.argv[2]);
if (nArgs) {
  for (let i = 0; i < nArgs; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
