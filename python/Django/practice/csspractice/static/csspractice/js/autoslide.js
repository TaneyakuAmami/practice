//参考:https://junpei-sugiyama.com/slick-loop/#google_vignette
$(function(){
    $('.slider').slick({
        autoplay: true,
        autoplaySpeed: 0,
        speed: 5000,
        cssEase: "linear",
        slidesToShow: 1,
        swipe: false,
        arrows: false,
        pauseOnFocus: false,
        pauseOnHover: false,
        responsive: [
            {
                breakpoint: 750,
                settings: {
                    slidesToShow: 1,
                }
            }
        ]
    });
});