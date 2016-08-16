#!/usr/bin/perl -wT

use CGI qw(:cgi-lib :standard);
use CGI::Cookie;

my $name = param("username");

$cookie_name = 'ID_cookie';
my $ID_var = CGI::Cookie->new(-name=>$cookie_name, -value=>$name, -expires => '1h', -httponly => 1);

print redirect(-url=>'session1_CGI.html', -cookie=>$ID_var);
