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



    // hide cars image when open description
    $('.collapsible').click(function () {
        $('.card-image').toggle();
    });
    $('.collapsible').collapsible();
});

function flash_icon() {
    $('.material-icons').fadeOut(1000);
    $('.material-icons').fadeIn(1000);
}
setInterval(flash_icon, 5500);

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


