#!/usr/bin/perl -wT

use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use strict;

my $name= param("username");

if( $name eq ''){
		print "<p>Howdy stranger, return to page 1 to input a username!</p>";
}
else{

	print <<EndOfHTML;
	<h2></h2>
	<p> Hi $name, nice to meet you </p>

	<button type="button"><a href="session1_CGI.html"> Back to Session1 CGI </a></button>
	<button type="button"><a href="session2_CGI.cgi"> Go to Session2 CGI </a></button>

	EndOfHTML

	print end_html;
}