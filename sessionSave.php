<?php
	session_start();
	$_SESSION["name"] = $_GET["username"];
	$name = $_SESSION["name"];
	header( 'Location: session1_PHP.html' )
?>