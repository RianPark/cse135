#!/usr/bin/perl 
use CGI qw(:cgi-lib :standard);
use CGI::Cookie;

%cookie_check = CGI::Cookie->fetch;
$cookie_var = $cookie_check{'ID_cookie'};

if ($cookie_var) 
{ 
	$name = $cookie_var->value;
	$state = "Hi $name nice to meet you";
}
else {
	$state = "Howdy stranger, tell me your name on session 1!";
}

print "Content-type: text/html\n\n"; 

print << "EOF";
<html>
	<head>
		<title>Session Page 2</title>
	</HEAD>
	<body>
		<H1>$state</H1>
		<button type="button"><a href="session1_CGI.html">Back to session 1</a></button>
		<button type="button"><a href="delete_CGI.cgi">Delete</a></button>
	</body>
</html>
EOF