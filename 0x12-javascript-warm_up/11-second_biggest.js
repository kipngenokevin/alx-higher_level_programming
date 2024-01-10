#!/usr/bin/node
// searches the second biggest integer in the list of arguments.

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const integers = process.argv.slice(2).map(Number);
  const sortedIntegers = integers.sort((a, b) => b - a);
  console.log(sortedIntegers[1]);
}
