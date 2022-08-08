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
    document.getElementById("tshirtlink").textContent=window.location.href;
});