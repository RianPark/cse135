<?php
	header('Content-Type: text/html'); 
	echo "<html><head><title>Environment Variables</title></head><body>";
	echo "<h1>Environment Variables : PHP</h1><pre>";
	print_r($_SERVER);
	echo"</body></html>";
?>