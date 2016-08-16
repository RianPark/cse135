var http = require("http");
var fs = require('fs');

http.createServer(function (request, response) {

	fs.readFile('blueJS.html', function(err, data) => {
		console.log(data);
	});

   response.writeHead(200, {'Content-Type': 'text/plain'});
   res.edn(data);
   
}).listen(8000);

// Console will print the message
console.log('Server running ');