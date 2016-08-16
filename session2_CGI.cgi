#!/usr/bin/perl -wT

use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use strict;

my $name= param("username");
my $cookie = cookie(-name=>'mycookie', -value=>$name );
my $state = 'aa';

if( $name eq ''){
		$state = 'Howdy stranger, return to page 1 to input a username!';
}
else{
		$state = 'Hi $name, nice to meet you';
}

print header(-cookie=>$cookie);
print start_html("Cookie");
print <<EndOfHTML;

<h2></h2>
 $state <p>

<button type="button"><a href="session1_CGI.html"> Back to Session1 CGI </a></button>
<button type="button"><a href="session2_CGI.cgi"> Go to Session2 CGI </a></button>
EndOfHTML
print end_html;
