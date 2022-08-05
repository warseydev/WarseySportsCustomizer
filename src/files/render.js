var slider = document.getElementById("sliderImages");
var sliderIndex = document.getElementById("sliderIndex");
var slidingImages = slider.children;
var amountOfImages = slidingImages.length;
var increment = 100 / amountOfImages;

slider.style.width = 100 * amountOfImages + "%";
slider.style.transform = "translateX(0%)";

