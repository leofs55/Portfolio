const carouselTrack = document.querySelector('.cards');
const carouselSlides = document.querySelectorAll('.card');
const prevButton = document.querySelector('.carousel-prev');
const nextButton = document.querySelector('.carousel-next');

let currentSlide = 0;

function goToSlide(index) {
    const slideWidth = carouselSlides[0].offsetWidth;
    const translateX = -slideWidth * index;

    carouselTrack.style.transform = `translateX(${translateX}px)`;
    currentSlide = index;
}

function nextSlide() {
    currentSlide++;
    if (currentSlide >= carouselSlides.length) {
    currentSlide = 0;
    }
    goToSlide(currentSlide);
}

function prevSlide() {
    currentSlide--;
    if (currentSlide < 0) {
    currentSlide = carouselSlides.length - 1;
    }
    goToSlide(currentSlide);
}

prevButton.addEventListener('click', prevSlide);
nextButton.addEventListener('click', nextSlide);

// Inicia o carrossel na primeira slide
goToSlide(0);