#!/usr/bin/perl -wT

use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use strict;

&ReadParse(%in);
my $cid = $in("username");
my $cookie = cookie(-name=>'mycookie', -value=>$cid, -domain=>'.cgi101.com');
print header(-cookie=>$cookie);
print start_html("Cookie");

print <<EndOfHTML;
<h2></h2>
Your name is $cid.<p>
EndOfHTML

print end_html;
redirect("session1_CGI.html");
