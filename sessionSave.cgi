#!/usr/bin/perl -wT
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use strict;

my $cid = int(rand(1000000));
my $cookie = cookie(-name=>'mycookie', -value=>$cid, -domain=>'.cgi101.com');
print header(-cookie=>$cookie);
print start_html("Cookie");

print <<EndOfHTML;
<h2>Welcome!</h2>
Your cookie is $cid.<p>
EndOfHTML

print end_html;
