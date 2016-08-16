<?php
	header('Content-Type: text/html');
	echo "<html><head><title>Form Echo</title>";
	
	$color=$_GET["color"];
	echo "</head><body bgcolor=$color><h1>";
	
	$firstname=$_GET["firstname"];
	$lastname=$_GET["lastname"];
	
	echo "<p>Hello $firstname $lastname from a Web app written in PHP on </p>"
	echo "<p>date time :".date("Y-m-d h:i:sa");
	
	echo "</p></h1></body></html>";
?>
