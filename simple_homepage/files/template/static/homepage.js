window.onload = function(){
     choosePic();
}

function choosePic() {
     var randomNum = Math.floor(Math.random() * images.length);
     document.getElementById("center-image").src = images[randomNum];
}
