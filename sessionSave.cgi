#!/usr/bin/perl -wT
use strict;

&ReadParse(%in);

my $cid = $in{username};

print "Set-Cookie: NAME=$cid\n";
print "Content-type: text/html\n\n";    

print <<EndOfHTML;
<html><head><title>Welcome</title></head>
<body>
<h2>Welcome!</h2>
Your cookie is $cid.<p>
</body></html>
EndOfHTML
;