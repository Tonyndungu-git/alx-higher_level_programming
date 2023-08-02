/* translates data fetched from a url 9-script.js */
$(document).ready(function() {
    $.getJSON("https://fourtonfish.com/hellosalut/?lang=fr")
    .done(function(data) {
        $("#hello").text(data.hello);
    })
    .fail(function() {
        $("#hello").text("Failed to fetch translation.");
    });
});
