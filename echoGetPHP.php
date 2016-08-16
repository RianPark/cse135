<?php
	$color=$_GET["color_select"];
	$first=$_GET["firstname"];
	$last=$_GET["lastname"];
	header('Content-Type: text/html');

	echo "<html><head><title>Form Echo</title>";
	echo "</head><body bgcolor=$color><h1>";
	echo "Hello $first $last, Web app with PHP, get method, on ".date("Y-m-d h:i:sa");
	echo "</h1></body></html>";
?>