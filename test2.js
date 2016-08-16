var express = require('express');
var app = express();
var fs = require('fs');

app.listen(8000, function() {
	console.log("start server");
})

app.get('/', function( req, res) {

	fs.readFile('blueJS.html', function(error, data) {
		if(error){
			console.log(error);
		} else {
			res.writeHead(200,{'Content-Type': 'text/html'});
			res.end(data);
		}
	});
});