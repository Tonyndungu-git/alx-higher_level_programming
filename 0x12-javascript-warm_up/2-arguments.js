#!/usr/bin/node
const args = process.argv.split(2);
const numberOfArguments = args.length;

if (numberOfArguments === 0) {
  console.log("No argument");
} else if (numberOfArguments === 1) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}
