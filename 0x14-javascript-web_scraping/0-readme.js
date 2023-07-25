#!/usr/bin/node

/* read file */
const req = require('fs');
const filepath = process.argv[2];

req.readFile(filepath, 'utf-8', (err, content) => {
  if (err) {
    console.error(err);
  } else {
    console.log(content);
  }
});
