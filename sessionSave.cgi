#!/usr/bin/perl
use strict;
use warnings;
use CGI;

my $cgi = CGI->new;
my $cookie = $cgi->cookie(
    -name  => 'User_cookie',
    -value => 'username'
);

print $cgi->header( -cookie => $cookie );
my $cookie_data = $cgi->cookie('value') || 'No Cookie Set';
print "<h2>Cookie Data: $cookie_data</h2>\n";