#!/usr/bin/perl -wT

use CGI qw(:cgi-lib :standard);

print "Content-type: text/html\n\n";

&ReadParse(%in);
$time = localtime();
$first = $in{"firstname"};
$last = $in{"lastname"};
$color = $in{"color_select"};

print << "EOF";
<HTML>
<HEAD>
<STYLE>
body {background-color: $color;}
</STYLE>
<TITLE>Form Results</TITLE>
</HEAD>
<BODY>
<H2>Hello $first $last, Web app with CGI, get method on $time\n</H2>
</BODY>
</HTML>
EOF