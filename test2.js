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
	console.log("start");
})

app.get('/', function( req, res) {

	if( num == 1){
		fs.readFile('redJS.html', function(error, data)
	}
	else if( num == 2 ){
		fs.readFile('blueJS.html', function(error, data)
	}
	else{
		fs.readFile('whiteJS.html', function(error, data)
	}
	res.end(data)
	});
});