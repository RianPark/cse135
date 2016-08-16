<DOCTYPE html>
<html>
	<head>
    	<title>Session2</title>
	</head>
	<body>
		<h1>Session2 : PHP</h1>
		<?php
        	session_start();
        	$name = $_SESSION['name'];
        	
        	if(isset($_SESSION['name']))
        	{
        		print "Hi ". $name . " nice to meet you!";
			}
			else
			{
        		print "Howdly stranger, tell me your name on session 1!";
			}
 		?>
  		<button type="button"><a href="delete_PHP.php" >Delete</a></button>
  		<button type="button"><a href="session1_PHP.html">Return to session 1</a></button>
	</body>
</html>
