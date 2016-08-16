<?php
	header('Content-Type: text/html'); 
	echo "<html><head><title>Environment Variables</title>";
	echo "</head><body>";
	echo "<h1>Environment Variables : PHP</h1>";
	echo "<pre>";
	print_r($_ENV);
	echo"</body></html>";
?>