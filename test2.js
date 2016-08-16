var http = require("http");

http.createServer(function (request, response) {

	fs.readFile('/blueJS.html', (err, data) => {
		if( err ) throw err;
		console.log(data);
	});

   response.writeHead(200, {'Content-Type': 'text/plain'});
   
   response.end('Hello World\n');
}).listen(8000);

// Console will print the message
console.log('Server running ');