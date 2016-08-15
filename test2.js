var express = require('express');
var app = express();
var fs = require('fs');

app.listen(3303, function() {
	console.log("start");
})

app.get('/', function( req, res) {
	fs.readFile('redJS.html', function(error, data) {
	res.end(data)
	});
});