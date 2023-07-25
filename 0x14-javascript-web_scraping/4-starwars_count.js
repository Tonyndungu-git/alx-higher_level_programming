#!/usr/bin/node

/*  prints the number of movies where the character id is present */
const req = require('request');
const apiUrl = process.argv[2];
const characterId = 18;
const characterUrl = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;

req.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
	const films = JSON.parse(body).results;
	      const numberOfMovies = films.filter(film => film.characters.includes(characterUrl)).length;
      console.log(numberOfMovies);
    } else {
      console.error('Failed to fetch data:', response.statusCode);
    }
  }
});
