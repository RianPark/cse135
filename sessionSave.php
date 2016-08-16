<?php
	session_start();
	$session["name"] = $_GET["username"];
	$name = $session["name"];
	header( 'Location: session1_PHP.html' )
?>