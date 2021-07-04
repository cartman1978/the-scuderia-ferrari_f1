$(document).ready(function () {
    $(".button").click(function () {
        $(".modal").removeClass("is-active");
        var Type = $(this).data("modal-type");
        $("#" + Type).addClass("is-active");
    });
});



