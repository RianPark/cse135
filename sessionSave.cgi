#!/usr/bin/perl -wT

use CGI qw(:cgi-lib :standard);

print "Content-type: text/html\n\n";

&ReadParse(%in);

$q = CGI->new();

$session = CGI::Session->new($q);

$name = param("username");
$id = $session -> id;
$cookie = $q ->cookie("CGISESSID", $id);
$session ->param('username', $name);
$user = $session -> param("username");

print << "EOF";
<html>
	<head>
		<title>Session Save CGI<title>
	</head>
	<body>
		<h1>Username $user was saved in a session</h1>
		<a href='session1_CGI.html'>Link Back to Page 1</a><br>
		<a href='sessionpage2.cgi'>Link to Page 2</a>
	</body>
</html>
EOF