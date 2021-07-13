$(document).ready(function () {

    $(".button").click(function () {
        $(".modal").removeClass("is-active");
        var Type = $(this).data("modal-type");
        $("#" + Type).addClass("is-active");
    });

});

$(".navbar-burger").click(function () {
    // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
    $(".navbar-burger").toggleClass("is-active");
    $(".navbar-menu").toggleClass("is-active");
});

$(document).ready(function () {
    $("button").click(function () {
        $('.hidden').hide();
        $(this).next().toggle();
    });
});



