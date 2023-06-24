// Carousel

const carousel = document.querySelector(".carousel_container");
const carouselContainer = carousel.querySelector(".carousel");
const carouselItems = carousel.querySelectorAll(".carousel-item");

const cloneItems = Array.from(carouselItems).map(item => item.cloneNode(true));
cloneItems.forEach(cloneItem => carouselContainer.appendChild(cloneItem));

carousel.addEventListener('scroll', () => {
  const scrollPosition = carousel.scrollLeft;
  const itemWidth = carouselItems[0].offsetWidth + parseInt(getComputedStyle(carouselItems[0]).marginRight);
  const totalWidth = carouselContainer.offsetWidth;

  if (scrollPosition + carousel.offsetWidth >= carousel.scrollWidth) {
    carousel.scrollLeft = 0;
  } else if (scrollPosition === 0) {
    carousel.scrollLeft = carousel.scrollWidth - carousel.offsetWidth;
  }
});

// Search

function handleKeyPress(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    performSearch();
  }
}

function performSearch() {
  const searchInput = document.querySelector('.search-input');
  const searchTerm = searchInput.value;

  console.log('Performing search for:', searchTerm);
}

