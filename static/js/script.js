$(document).ready(function () {
    $('.modal').modal();


});


$(document).ready(function () {
    $("button").click(function () {
        $('.hidden').hide();
        $(this).next().toggle();
    });

});


$(document).ready(function () {
    $('.sidenav').sidenav();
});

$(document).ready(function () {
    $('.collapsible').collapsible();
});

