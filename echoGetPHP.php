<?php
	header('Content-Type: text/html');
	echo "<html><head><title>Form Echo</title>";
	$color=$_GET["color"];
	echo "</head><body bgcolor=$get_color><h1>";
	$first=$_GET["firstname"];
	$last=$_GET["lastname"];
	$dtime= date("Y-m-d", time());
	$theTime= time();
	echo "<p>Hello $first $last from a Web app written in PHP on </P>";
	echo "<p> .date("Y-m-d h:i:sa")";
	echo "</h1></p></body></html>";
?>