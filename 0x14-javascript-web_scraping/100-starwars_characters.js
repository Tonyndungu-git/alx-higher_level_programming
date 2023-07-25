#!/usr/bin/node

/* script that prints all characters of a Star Wars movie */
const req = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

req.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data:', response.statusCode);
    return;
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  characters.forEach((characterUrl) => {
    req.get(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
      } else if (response.statusCode === 200) {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      } else {
        console.error('Failed to fetch character data:', response.statusCode);
      }
    });
  });
});
