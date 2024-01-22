// Copy size of slider


function copyDimensions() {
  var sourceElement = document.getElementById("container");
  var targetElement = document.getElementById("slider");

  targetElement.style.width = sourceElement.offsetWidth + "px";
  targetElement.style.height = sourceElement.offsetHeight + "px";

  var rect = sourceElement.getBoundingClientRect();
  var xOffset = sourceElement.offsetWidth;
  var yOffset = sourceElement.offsetHeight;


}

//Center Images


function centerElements() {
    for (var i = 1; i <= urls_length; i++) {
        var sourceElement = document.getElementById("photo_container");
        var targetElement = document.getElementById("image" + i);

        var offsetX = (sourceElement.offsetWidth - targetElement.offsetWidth) / 2;
        var offsetY = (sourceElement.offsetHeight - targetElement.offsetHeight) / 2;

        targetElement.style.left = offsetX + "px";
        targetElement.style.top = offsetY + "px";
    }
}

centerElements();

//Image slider logics


imageIndex = 1;

document.getElementById("image1").classList.remove('disabled');



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

