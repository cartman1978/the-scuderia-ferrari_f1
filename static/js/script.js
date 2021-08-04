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

    // Logo fade in
    $('#logo').fadeIn(1000, function () {
        $(this).animate({ "left": "35px" }, 2000);
    });


    // hide cars image when open description
    $('.collapsible').click(function () {
        $('.card-image').toggle();
    });
    $('.collapsible').collapsible();
});


var $descriptions = $('.material-icons');
var i = 0;
setInterval(function () {
    $descriptions.removeClass('multiCol');
    $($descriptions[i]).addClass('multiCol');
    i++;
    if (i === $descriptions.length) i = 0;
}, 700)

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


