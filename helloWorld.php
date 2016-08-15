
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
echo "</head><body bgcolor =$color>";
echo "<p>Hello World : PHP</p>";
echo "<p>Date, time : ".date("Y-m-d h:i:sa");
echo"</p></body></html>";
?>