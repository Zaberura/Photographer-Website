// NavBar changing current tab style

document.addEventListener("DOMContentLoaded", function() {
  var baseUrl = "http://127.0.0.1:5000/";
  var navLinks = document.querySelectorAll(".nav_item");

//  navLinks.forEach(function(link) {
//    link.addEventListener("click", function() {
//      navLinks.forEach(function(link) {
//        link.classList.remove("nav_active");
//      });
//
//      this.classList.add("nav_active");
//    });
//  });

  var currentLocation = window.location.href;
  navLinks.forEach(function(link) {
    if(currentLocation === baseUrl && link.href === baseUrl){
        link.classList.add("nav_active");

    } else {
        if (currentLocation.startsWith(link.href) && link.href != baseUrl) {
          link.classList.add("nav_active");
        } else {
          link.classList.remove("nav_active");
        };
    }

  });
});
