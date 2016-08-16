#!/usr/bin/perl -wT

use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use strict;

my $name = param("username");
my $state = 'aa';

if( $name == ''){
		$state = 'Howdy stranger, return to page 1 to input a username!';
}
else{
		$state = 'Hi $name, nice to meet you';
}

print header;
print start_html("");
print <<EndOfHTML;

<h2></h2>
 <p> $state .. </p>
 <p> $name  .. </p>

<button type="button"><a href="session1_CGI.html"> Back to Session1 CGI </a></button>
<button type="button"><a href="session2_CGI.cgi"> Go to Session2 CGI </a></button>
EndOfHTML
print end_html;
