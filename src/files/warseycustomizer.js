window.serverurl="https://api.warsey.com";
window.model="none";
window.name="Your Name Here";
var lastentry = "";
$("#model").chained("#country");

function ChangeModel(e) {
    if (e.target.value == "none") {
        return
    }
    text=encodeURIComponent(window.name);
    style="background-image: url('"+window.serverurl+"/api/design/tshirt?text="+text+"&template="+e.target.value+"');-webkit-transition: all 1s ease-in-out;-moz-transition: all 1s ease-in-out;-o-transition: all 1s ease-in-out;-ms-transition: all 1s ease-in-out;";
    document.getElementById("tshirt").style=style;
    window.model=e.target.value;
}

$('#name').keyup(function(event) {
    if (window.model == "none") {
        return
    }
    if ($('#name').val() == "") {
        EmptyName();
        return
    }
    if($('#name').val() != lastentry) {  
        window.name=$('#name').val();  
        text=encodeURIComponent(text);
        style="background-image: url('"+window.serverurl+"/api/design/tshirt?text="+text+"&template="+window.model+"');-webkit-transition: all 1s ease-in-out;-moz-transition: all 1s ease-in-out;-o-transition: all 1s ease-in-out;-ms-transition: all 1s ease-in-out;";
        document.getElementById("tshirt").style=style;
        window.name=text;
    }
    lastentry = $('#name').val();
});

function EmptyName() {
    if (window.model == "none") {
        return
    }
    style="background-image: url('"+window.serverurl+"/api/design/tshirt?text=Your%20Name%20Here&template="+window.model+"');-webkit-transition: all 1s ease-in-out;-moz-transition: all 1s ease-in-out;-o-transition: all 1s ease-in-out;-ms-transition: all 1s ease-in-out;";
    document.getElementById("tshirt").style=style;
    window.name="Your Name Here";
}

function GenerateShareCode() {
    if (window.model == "none" || window.name == "Your Name Here") {
        swal({title: "You haven't customized your T-shirt", text: "Customize your T-Shirt in order to get a share code.", dangerMode: true});
        return
    }
    text=encodeURIComponent(window.name);
    let createlink="/create?name="+text+"&model="+window.model;
    window.location.replace(createlink);   
}

function RevertToNone() {
    style="background-image: url('/content/none.webp');-webkit-transition: all 1s ease-in-out;-moz-transition: all 1s ease-in-out;-o-transition: all 1s ease-in-out;-ms-transition: all 1s ease-in-out;";
    document.getElementById("tshirt").style=style;
    window.model="none";
}

$(document).ready(function() {
    var opt = $("#countrylist option").sort(function (a,b) { return a.value.toUpperCase().localeCompare(b.value.toUpperCase()) });
    $("#countrylist").append(opt);
    $("#countrylist").find('option:first').attr('selected','selected');
});