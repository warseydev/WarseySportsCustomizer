function copyToClipboard() {
    var text = document.getElementById('codeshare').innerHTML;
    var tempTextbox = document.getElementById('copyingText');
    tempTextbox.style="visibility: visible;"
    tempTextbox.value = text;
    tempTextbox.focus();
    tempTextbox.select();
    document.execCommand("Copy");
    tempTextbox.style="visibility: hidden;"
    CopiedAnimation();
}

function CopiedAnimation() {
    document.getElementById("copynotif").classList.add("copyanimation");
    setTimeout( function() {
        document.getElementById("copynotif").classList.remove("copyanimation");
    }, 1000);
}

$(document).ready(function(){                                
    var sharecode = document.getElementById("sharecodep").textContent;
    let shareurl=window.location.origin+"/s/"+sharecode; 
    document.getElementById("tshirtlink").textContent=shareurl;
    var qrc = new QRCode(document.getElementById("qrcode"), {
        text: shareurl,
        width: 100,
        height: 100,
        colorDark: "#1E9738",
        colorLight: "#2b2b2b",
        correctLevel : QRCode.CorrectLevel.H
      });
});