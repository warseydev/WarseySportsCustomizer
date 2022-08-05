function copyToClipboard() {
    var text = document.getElementById('codeshare').innerHTML;
    var tempTextbox = document.getElementById('copyingText');
    tempTextbox.style="visibility: visible;"
    tempTextbox.value = text;
    tempTextbox.focus();
    tempTextbox.select();
    document.execCommand("Copy");
    tempTextbox.style="visibility: hidden;"
    console.log('done');
}