/* creating an event listener  that changes colour*/
$(document).ready(function() {
    $("DIV#red_header").on("click", function() {
        $("header").css("color", "#FF0000");
    });
});
