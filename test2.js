var express = require('express');
var app = express();
var fs = require('fs');

var num;
var low = 1;
var high = 3;

function randomInt ( low, high ) {
	num = Math.floor(Math.random() * ( high -low ) + low );
}

app.listen(3303, function() {
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