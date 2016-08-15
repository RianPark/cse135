var http = require("http");

http.createServer(function (request, response) {

   // Send the HTTP header 
   // HTTP Status: 200 : OK
   // Content Type: text/plain
   response.writeHead(200, {'Content-Type': 'text/plain'});
   
   // Send the response body as "Hello World"
   response.end('Hello World JS\n');
}).listen(8000);

// Console will print the message
console.log('Hello World running at http://138.68.30.229:8000/');

setTimeout(function() {
	util.puts('Throwing error now.');
	throw new Error('User generate fault.');
}, 5000);