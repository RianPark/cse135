#!/usr/bin/perl -wT

use CGI qw(:cgi-lib :standard);

print "Content-type: text/html\n\n";

&ReadParse(%in);
$first = $in{"firstname"};
$last = $in{"lastname"};
$color = $in{"color_select"};

$time = localtime();

print << "EOF";
<html>
	<head>
		<style>
			body {background-color: $color;}
		</style>
		<title>Form Results</title>
	</head>
	<body>
		<h2>Hello $first $last, Web app CGI with post, on $time\n</h2>
	</body>
</html>
EOF