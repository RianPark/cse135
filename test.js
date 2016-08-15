var http = require("http");
var color;

function random (0, 2) {
    num =  Math.random() * 2 ;
}

http.createServer(function (request, response) {

   // Send the HTTP header 
   // HTTP Status: 200 : OK
   // Content Type: text/plain
   response.writeHead(200, {'Content-Type': 'text/plain'});

   var bgblue = require('ansi-bgblue');
 
   console.log(colors.bgblue());
   response.end('Hello World JS\n');
}).listen(8000);

// Console will print the message
console.log('Hello World running at http://138.68.30.229:8000/');