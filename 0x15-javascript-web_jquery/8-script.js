/* fetches and lists the title for all movies by using a URL 8-script.js */
$(document).ready(function() {
    $.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json",
	      function(data) {
        const listElement = $("#list_movies");
        data.results.forEach(function(movie) {
            const title = movie.title;
            listElement.append($("<li>").text(title));
        });
    });
});
