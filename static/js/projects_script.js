const carousel = document.querySelector(".carousel");
const carouselContainer = carousel.querySelector(".carousel-container");
const carouselItems = carousel.querySelectorAll(".carousel-item");

// Clone and append the initial items to the end of the carousel
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

function handleKeyPress(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    performSearch();
  }
}

function performSearch() {
  const searchInput = document.querySelector('.search-input');
  const searchTerm = searchInput.value;



  // Perform search with the searchTerm
  // Replace the console.log() statement with your search logic
  console.log('Performing search for:', searchTerm);
}

