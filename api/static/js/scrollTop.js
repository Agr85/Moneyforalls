$(document).ready(function () {
    $('.goup').hide();
    $('.goup').click(function () {
        $('body,html').animate({
            scrollTop: 0
        }, 800)
    });

    $(window).scroll(function () {
        if ($(this).scrollTop() > 200) {
            $('.goup').fadeIn();
        } else {
            $('.goup').fadeOut();
        }
    });

});

/* var rocket = document.querySelector('.goup');

rocket.addEventListener('click', function () {

    this.classList.toggle('clicked');

}); */