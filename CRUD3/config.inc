<?php

    define('DB_USER','root');
    define('DB_PASSWORD','Jh272618');
    define('DB_HOST','localhost');
    define('DB_NAME','first');

	$conn = mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);
    
    if (!$conn) {
      die("Connection failed: " . mysqli_connect_error());
    }
?>
