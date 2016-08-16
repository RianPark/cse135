#!/usr/bin/perl 
use CGI qw(:cgi-lib :standard);
use CGI::Cookie;

%do_you_haz_cookie = CGI::Cookie->fetch;
$da_cookie = $do_you_haz_cookie{'DA_BEST_COOKIE_EVA'};
if ($da_cookie) { 
	$users_name = $da_cookie->value;
	$output_msg = "Hi $users_name nice to meet you";
}
else {
	$output_msg = "Howdy stranger...tell me your name on page1!";
}

print "Content-type: text/html\n\n"; 

print << "EOF";
<HTML>
<HEAD>
<title>Session Page 2</title>
</HEAD>
<BODY>
<H1>$output_msg</H1>
<a href="session1_CGI.html">Back to page one</a><br>
<a href="delete_CGI.cgi">Clear Session</a>
</BODY>
</HTML>
EOF