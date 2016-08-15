
<?php
	header('Content-Type: text/html'); 
	echo "<html><head><title>Hello World</title>";
	
	$num = rand(0, 2);
	$color = white;
	
	if($num == 0)
	{
		$color = red;
	}
	elseif($num == 1)
	{
		$color = white;
	}
	else
	{
		$color = blue;
	}
echo "</head><body bgcolor =$color><h1>";
echo "Hello World : PHP \n
";
echo "Date, time : ".date("Y-m-d h:i:sa") .PHP_EOL;
echo"</body></html>";
?>