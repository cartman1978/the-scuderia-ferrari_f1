$(document).ready(function () {
    $('.modal').modal();
    $("button").click(function () {
        $('.hidden').hide();
        $(this).next().toggle();
    });
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('.container').mouseenter(function () {
        $('p').css("font-weight", "500");
    });
    setTimeout(function () {
        $('.zoom').fadeIn(3000);
    }, 3000);
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


