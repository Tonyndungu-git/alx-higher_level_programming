/* adding a row on a list 5-script.js */
$(document).ready(function() {
    $("DIV#add_item").on("click", function() {
        $("ul.my_list").append($("<li>").text("Item"));
    });
});
