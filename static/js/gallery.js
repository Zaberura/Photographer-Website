// Copy size of slider

function copyDimensions() {
  var sourceElement = document.getElementById("image1");
  var targetElement = document.getElementById("slider");

  targetElement.style.width = sourceElement.offsetWidth * 1.16 + "px";
  targetElement.style.height = sourceElement.offsetHeight * 1.16 + "px";
}



document.getElementById("image1").classList.remove('disabled');

//Image slider logics

imageIndex = 1;

function next_img() {

    document.getElementById("image" + imageIndex).classList.add('disabled');
    if (imageIndex >= urls_length){ imageIndex = 0 ;}
    document.getElementById("image" + (imageIndex + 1)).classList.remove('disabled');

    imageIndex++;
}

function prev_img() {

    document.getElementById("image" + imageIndex).classList.add('disabled');
    if (imageIndex <= 1){ imageIndex = urls_length + 1;}
    document.getElementById("image" + (imageIndex - 1)).classList.remove('disabled');

    imageIndex--;
}

// Set Event Listeners on clicks 'n' keys

document.getElementById("slider_right").addEventListener("click", next_img);
document.getElementById("slider_left").addEventListener("click", prev_img);

document.addEventListener("keydown", function(event) {
  if (event.code === "Space" || event.keyCode === 39) {
    event.preventDefault();
    next_img();
  } else if (event.keyCode === 37) {
    prev_img();
  }
});


copyDimensions();

