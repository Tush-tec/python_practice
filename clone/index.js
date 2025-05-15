 const menuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  menuBtn.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
});


const openBtn = document.getElementById('open-search');
const closeBtn = document.getElementById('close-search');
const modal = document.getElementById('search-modal');

openBtn.addEventListener('click', () => modal.classList.remove('hidden'));
closeBtn.addEventListener('click', () => modal.classList.add('hidden'));

// Optional: Close on ESC key or clicking outside the box
modal.addEventListener('click', (e) => {
  if (e.target === modal) modal.classList.add('hidden');
});
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') modal.classList.add('hidden');
});


const swiper = new Swiper(".mySwiper", {
    loop: true,
    autoplay: {
      delay: 3500,
      disableOnInteraction: false,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    effect: "fade",
    speed: 900,
});


function toggleSubcategory(id) {
  // Hide all subcategory overlays first
  document.querySelectorAll('[id$="-subcategory"]').forEach(el => el.classList.add('hidden'));
  // Show the selected one (toggle)
  const selected = document.getElementById(id + '-subcategory');
  if (selected) selected.classList.toggle('hidden');
}

 


 const featuredProductsSwiper = new Swiper('.featuredProductsSwiper', {
    slidesPerView: 1.2,
    spaceBetween: 24,
    loop: true,
    speed: 900,
    autoplay: {
      delay: 1800,
      disableOnInteraction: false,
      pauseOnMouseEnter: true, // Swiper 9+ supports this
    },
    breakpoints: {
      640: {
        slidesPerView: 2.2,
      },
      1024: {
        slidesPerView: 3.2,
      }
    },
    grabCursor: true,
    a11y: {
      enabled: true,
      prevSlideMessage: 'Previous product',
      nextSlideMessage: 'Next product',
      firstSlideMessage: 'This is the first product',
      lastSlideMessage: 'This is the last product',
      paginationBulletMessage: 'Go to product {{index}}',
      slideLabelMessage: '{{index}} / {{slidesLength}}',
    },
    keyboard: {
      enabled: true,
      onlyInViewport: true,
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
      renderBullet: function (index, className) {
        return `<button class="${className}" aria-label="Go to product ${index + 1}"></button>`;
      }
    },
  });



    