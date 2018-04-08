var titleBlock = document.getElementById('titleBlock');
var searchButton = document.getElementById('searchButton');
var category1 = document.getElementById('formInputCategory1');



function submitClick() {
    alert("yodel")
    document.getElementById('searchResults').style.display = "block";
    document.getElementById('searchResults').scrollIntoView();
};


//searchButton.addEventListener("click", setTimeout(submitClick, 500));