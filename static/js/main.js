// Copy size of slider

function copyDimensions() {
  var sourceElement = document.getElementById("image");
  var targetElement = document.getElementById("slider");

  targetElement.style.width = sourceElement.offsetWidth + "px";
  targetElement.style.height = sourceElement.offsetHeight + "px";
}

