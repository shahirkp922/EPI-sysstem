$(document).ready(function(){
    $('#myCarousel').on('slide.bs.carousel', function (e) {
        var $next = $(e.relatedTarget);
        var currentIndex = $(e.target).find('.active').index();
        var nextIndex = $next.index();
        
        if (nextIndex > currentIndex) {
            $(e.target).find('.carousel-inner').css('transform', 'translateX(-100%)');
        } else {
            $(e.target).find('.carousel-inner').css('transform', 'translateX(100%)');
        }
    });
});