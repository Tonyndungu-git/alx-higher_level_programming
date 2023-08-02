/*  JavaScript script that fetches and
prints how to say “Hello” depending on the language */
$(document).ready(function() {
    function fetchTranslation() {
        var languageCode = $("#language_code").val();
        var apiUrl = "https://www.fourtonfish.com/hellosalut/hello/";

        $.getJSON(apiUrl, { lang: languageCode }, function(data) {
            $("#hello").text(data.hello);
        });
    }

    $("#btn_translate").click(fetchTranslation);

    $("#language_code").keypress(function(event) {
        if (event.keyCode === 13) {
            fetchTranslation();
        }
    });
});
