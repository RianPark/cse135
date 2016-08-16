#!/usr/bin/perl -wT
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use strict;

print header;
print start_html("Get/Post CGI");

my %form;
my $first = param('firstname');
my $last = param('lastname');
my $color = param('color_select');
my $time = localtime;

print "<body bgcolor = $color>";
print "<h1>Hello $first $last, Web app with CGI, get method on $time</h1>";
print "</body>";
print end_html;