#!/usr/bin/node

/* script that gets the contents of a webpage and stores it in a file */

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    fs.writeFile(filePath, body, { encoding: 'utf-8' }, (err) => {
      if (err) {
        console.error(err);
      } else {
        console.log(`Successfully saved the contents of ${url} to ${filePath}`);
      }
    });
  }
});
