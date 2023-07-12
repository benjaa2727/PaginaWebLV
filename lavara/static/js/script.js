
let images = document.querySelectorAll('#carousel img');
let index = 0;


function prevImage() {
  images[index].classList.remove('active');
  index = (index - 1 + images.length) % images.length;
  images[index].classList.add('active');
}


function nextImage() {
  images[index].classList.remove('active');
  index = (index + 1) % images.length;
  images[index].classList.add('active');
}


document.querySelector('.prev').addEventListener('click', prevImage);
document.querySelector('.next').addEventListener('click', nextImage);

const carousel = document.getElementById('carousel');
const carouselImages = carousel.getElementsByTagName('img');
let activeIndex = 0;

function changeImage() {
  
  carouselImages[activeIndex].classList.remove('active');

  
  activeIndex++;
  if (activeIndex >= carouselImages.length) {
    activeIndex = 0;
  }

  
  carouselImages[activeIndex].classList.add('active');
}


setInterval(changeImage, 6000);








