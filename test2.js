var http = require("http");
var fs = require('fs');

http.createServer(function (request, response) {

	<div style="background:yellow" ani_type="color(background:'red')"></div>
<br />
    response.writeHead(200, {'Content-Type': 'text/plain'});
    response.end('Hello World\n');
}).listen(8000);

// Console will print the message
console.log('Server running ');