#!/usr/bin/perl
use strict;
use warnings;
use CGI;

my $cgi = CGI->new;
my $cookie = $cgi->cookie(
    -name  => 'sithLord',
    -value => 'Darth Vadar'
);

print $cgi->header( -cookie => $cookie );
my $cookie_data = $cgi->cookie('sithLord') || 'Howdy stranger, return to page 1 to input a username!';
print "<h2>Cookie Data: $cookie_data</h2>\n";