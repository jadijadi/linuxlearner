$(document).ready(function(){
    /*toggle menu*/
    $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
    });

    /*smooth scroll toc*/
    $('a[href^="#"].toc-href').on('click',function (e) {
        e.preventDefault();

        var offset = 0
        var target = this.hash;
        if (target.length){
            offset = $(target).offset().top
        }

        $('html, body').stop().animate({
            'scrollTop': offset
        }, 500, 'swing', function () {
            window.location.hash = target;
        });
    });
});
