var express = require('express');
var app = express();
var path = require('path');
var num = 0;
var low = 1;
var high = 3;

function randomInt ( low, high ) {
	num = Math.floor(Math.random() * ( high -low ) + low );
}

app.get('/', function (request, response) {

   // Send the HTTP header 
   // HTTP Status: 200 : OK
   // Content Type: text/plain
   //response.writeHead(200, {'Content-Type': 'text/plain'});
   //var bgblue = require('ansi-bgblue');

   	if( num == 1)
	{
   		res.sendFile(path.join(__dirname + '/blueJS.html'));
	}
	else if(num == 2)
	{
   		res.sendFile(path.join(__dirname + '/whiteJS.html'));
	}
	else
	{
   		res.sendFile(path.join(__dirname + '/redJS.html'));
	}
});
app.listen(8000);

// Console will print the message
console.log('Hello World running at http://138.68.30.229:8000/');