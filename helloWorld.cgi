#!/usr/bin/perl

print "Content-type: text/html\n\n";

$time = localtime;
$colorChoice = int(rand(3));

if($colorChoice == 0){
	$color = red;
}
elsif($colorChoice == 1){
	$color = white;
}
else{
$color = blue;
}

print "<html><head><title>Hello World</title>";
print "</head><body bgcolor=$color>\n";
print "<p>Hello World : CGI </p>";
print "<p>Date, Time : $time\n</p>";
print"</body>\n</html>";

