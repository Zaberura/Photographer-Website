// NavBar changing current tab style

document.addEventListener("DOMContentLoaded", function() {
  var navLinks = document.querySelectorAll(".nav_item");

  navLinks.forEach(function(link) {
    link.addEventListener("click", function() {
      navLinks.forEach(function(link) {
        link.classList.remove("nav_active");
      });

      this.classList.add("nav_active");
    });
  });

  var currentLocation = window.location.href;
  navLinks.forEach(function(link) {
    if (link.href === currentLocation) {
      link.classList.add("nav_active");
    }
  });
});