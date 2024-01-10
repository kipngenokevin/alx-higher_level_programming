#!/usr/bin/node
const num = parseInt(process.argv[2]);
function numFactorial (a) {
  if (a === 0 || a === 1) {
    return 1;
  } else {
    return a * numFactorial(a - 1);
  }
}
if (num) {
  console.log(numFactorial(num));
} else {
  console.log(1);
}
