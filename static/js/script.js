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



jQuery(function ($) {
    $('.textillate-5').textillate({
        loop: true,
        minDisplayTime: 3000,
        initialDelay: 500,

        in: {
            effect: 'fadeIn', //EffectType(options;http://textillate.js.org/)
        }
    });
});


$(document).ready(function () {
    $('.container').mouseenter(function () {
        $('p').css("font-weight", "bold");
    });
});