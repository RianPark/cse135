<?php
	session_start();
	session_destroy();
	header( 'Location: session2_PHP.php' )
?>