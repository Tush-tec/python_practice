



document.addEventListener("DOMContentLoaded", function () {

 const swiper = new Swiper(".mySwiper", {
    loop: true,
    autoplay: {
      delay: 1000,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  })
})





  