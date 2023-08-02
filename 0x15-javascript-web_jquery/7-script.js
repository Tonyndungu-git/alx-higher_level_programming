/*fetches the character name from a URL 7-script.js */
$(document).ready(function() {
    $.getJSON("https://swapi-api.alx-tools.com/api/people/5/?format=json",
	      function(data) {
        $("#character").text(data.name);
    });
});
