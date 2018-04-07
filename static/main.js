//function loadDoc() {
//  var xhttp = new XMLHttpRequest();
//  xhttp.onreadystatechange = function() {
//    if (this.readyState == 4 && this.status == 200) {
//     document.getElementById("demo").innerHTML = this.responseText;
//    }
//  };
//  xhttp.open("GET", "goodSample.txt", true);
//  xhttp.send();
//}
var titleBlock = document.getElementById('titleBlock');
var searchButton = document.getElementById('searchButton');

//alert("hey");


//var category1 = document.getElementById('formInputCategory1');



function changeColor() {
    titleBlock.style.backgroundColor = "red";
    titleBlock.style.color = "red";
    alert("hey");
//    modalBackdrop.style.display = 'block';
//    twitModal.style.display = 'block';
};

//alert ("yo");

changeColor();

//titleBlock.addEventListener('click', changeColor);