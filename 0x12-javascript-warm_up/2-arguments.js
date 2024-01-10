#!/usr/bin/node
const { argv } = require('node:process');
let index = 0;
argv.forEach((val) => {
  index++;
});
if (index === 2) {
  console.log('No argument');
} else if (index === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
