$.get('./htmlOutput.txt', {}, function(content) {
    console.log(content);
});

const fileUrl = './htmlOutput.txt' // provide file location

fetch(fileUrl)
  .then(response => response.text())
  .then(data => {
  	console.log(data);
  });

//document.getElementById("examples")