#!/usr/bin/node

const arg = parseInt(process.argv[2]);

function factorial(n) {
  if (isNaN(n)) {
    return 1;
  }

  if (n === 0 || n === 1) {
    return 1;
  }

  return n * factorial(n - 1);
}

const result = factorial(arg);

console.log(result);
