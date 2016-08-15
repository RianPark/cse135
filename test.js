var http = require("http");
var num = 0;
var color;

function random (0, 2) {
    num =  Math.random() * 2 ;
}
eateServer(function (request, response) {

   // Send the HTTP header 
   // HTTP Status: 200 : OK
   // Content Type: text/plain
   response.writeHead(200, {'Content-Type': 'text/plain'});

   if( num == 0 )
   {
		var bgred = require('ansi-bgred');
   }
   else if( num == 1 )
   {
		var bgwhite = require('ansi-bgwhite');
   }   
   else
   {
		var bgblue = require('ansi-bgblue');
   }

   response.background()
   // Send the response body as "Hello World"
   response.end('Hello World JS\n');
}).listen(8000);

// Console will print the message
console.log('Hello World running at http://138.68.30.229:8000/');