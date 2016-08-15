var express = require('express');
var app = express();
var path = require('path');
var num = 0;

function randomInt ( 1, 3 ) {
	num = Math.floor(Math.random() * ( 3-1 ) + 1 );
}

app.get( function (request, response) {

   // Send the HTTP header 
   // HTTP Status: 200 : OK
   // Content Type: text/plain
   //response.writeHead(200, {'Content-Type': 'text/plain'});
   //var bgblue = require('ansi-bgblue');

   	if( num == 1)
	{
   		res.sendFile(path.join(__dirname + 'blueJS.html'));
	}
	else if(num == 2)
	{
   		res.sendFile(path.join(__dirname + 'whiteJS.html'));
	}
	else
	{
   		res.sendFile(path.join(__dirname + 'redJS.html'));
	}

})
app.listen(8000);

// Console will print the message
console.log('Hello World running at http://138.68.30.229:8000/');