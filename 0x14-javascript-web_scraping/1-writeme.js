#!/usr/bin/node

/* writing to a file using js */

const res = require('fs');
const filepath = process.argv[2];
const content = process.argv[3];

res.writeFile(filepath, content, 'utf-8', err => {
  if (err) {
    console.error(err);
  }
});
