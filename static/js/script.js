
$(document).ready(function () {

    // Modal for delete functions
    // https://stackoverflow.com/questions/27650584/multiple-modals#27650708
    $(".button").click(function () {
        $(".modal").removeClass("is-active");
        var Type = $(this).data("modal-type");
        $("#" + Type).addClass("is-active");
    });


});

