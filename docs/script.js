// Add the names generated with the Pyhton Script in the names.txt file
function read() {
  const names = new XMLHttpRequest();
  names.open("GET", "names.txt", true);
  names.onreadystatechange = function () {
    if (names.readyState === 4) {
      // Makes sure the document is ready to parse.
      if (names.status === 200) {
        document.getElementById("examples").innerHTML = names.responseText;
      }
    }
  };
  names.send(null);
}
read();
// Add random colors to the ASCII names
codecolors = ['deepskyblue', 'aquamarine', 'yellow', 'lime', 'fuchsia', 'orangered'];
let color = 0;
setInterval(function(){ 
    let codenames = document.getElementsByClassName("code");
    for (codename of codenames) {
      let currentColor = color % codecolors.length;
      codename.style.color = codecolors[currentColor];
      color += 1;
    }
}, 500);

document.getElementsByTagName('footer')[0].innerHTML += ' ' + new Date().getFullYear() + ' © All Rights Reserved, Huixquilucan MEX, Mexico';