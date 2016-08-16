<?php
	header('Content-Type: text/html');
	echo "<html><head><title>Form Echo</title>";
	$color=$_GET["color_select"];
	echo "</head><body bgcolor=$color><h1>";
	$first=$_GET["firstname"];
	$last=$_GET["lastname"];

	echo "<p>Hello $first $last from a Web app written in PHP </p>";
	echo "<p> on .date("Y-m-d h:i:sa") ";
	echo "</p></h1></body></html>";
?>