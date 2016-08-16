#!/usr/bin/perl -wT
use CGI qw(:cgi-lib :standard);
use CGI::Cookie;

%cookie_check = CGI::Cookie->fetch;
$cookie_var = $cookie_check{'ID_cookie'};
if ($cookie_var) 
{ 
	$cookie_var->expires('-1d');
	$cookie_var->value(' ');
}

print redirect(-url=>'session2_CGI.cgi', -cookie=>$cookie_var);