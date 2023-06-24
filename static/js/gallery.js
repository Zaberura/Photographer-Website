// Copy size of slider

function copyDimensions() {
  var sourceElement = document.getElementById("image");
  var targetElement = document.getElementById("slider");

  targetElement.style.width = sourceElement.offsetWidth * 1.16 + "px";
  targetElement.style.height = sourceElement.offsetHeight * 1.16 + "px";
}

function prev_img() {

    if(imageIndex <= 0){ imageIndex = urls.length -1; }
    else { imageIndex--; }

    image.classList.remove('notransition');
    image3.classList.remove('notransition');
    image.style.opacity = "0";
    image3.style.opacity = "1";

    setTimeout(function() {

        image.src = urls[imageIndex];

        if(imageIndex >= urls.length -1 ){
            image2.src = urls[0];
        } else {
            image2.src = urls[imageIndex + 1];
        }
        if(imageIndex <= 0 ){
            image3.src = urls[urls.length-1];
        } else {
            image3.src = urls[imageIndex -1];
        }

        image.classList.add('notransition');
        image3.classList.add('notransition');
        image.style.opacity = "1";
        image3.style.opacity = "0";

        //copyDimensions();
    }, 100);
}


function next_img() {

    if(imageIndex >= urls.length -1){ imageIndex = 0; }
        else { imageIndex++; }

    image.classList.remove('notransition');
    image2.classList.remove('notransition');
    image.style.opacity = "0";
    image2.style.opacity = "1";

    setTimeout(function() {

        image.src = urls[imageIndex];

        if(imageIndex >= urls.length -1 ){
            image2.src = urls[0];
        } else {
            image2.src = urls[imageIndex + 1];
        }
        if(imageIndex <= 0 ){
            image3.src = urls[urls.length-1];
        } else {
            image3.src = urls[imageIndex - 1];
        }

        image.classList.add('notransition');
        image2.classList.add('notransition');
        image.style.opacity = "1";
        image2.style.opacity = "0";

        //copyDimensions();
    }, 100);
}


copyDimensions();

let image = document.getElementById("image");
let image2 = document.getElementById("image_2");
let image3 = document.getElementById("image_3");
imageIndex = 0;

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


