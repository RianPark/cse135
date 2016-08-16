#!/usr/bin/perl -wT

use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use strict;

my $cid = param("username");
my $cookie = cookie(-name=>'mycookie', -value=>$cid );
print header(-cookie=>$cookie);
print start_html("Cookie");

print <<EndOfHTML;
<h2></h2>
Your name is $cid.<p>
EndOfHTML

<p><a href="session1_CGI.html"> Back to Session1 CGI </a></p>

<p><a href="session2_CGI.cgi"> Go to Session2 CGI </a></p>

print end_html;
