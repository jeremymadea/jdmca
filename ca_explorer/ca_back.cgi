#!/usr/bin/perl
use CGI;
$q = new CGI;

print "Content-type: text/html\n\n";

$time = time;

if (defined($q->param('p'))) {
    $p = $q->param('p');
    if ($p =~ /^(\d+)$/) {
        $p = $1;
    } else {
        $p = 50;
    }
    if ( ($p < 0) || ($p > 100) ) {
        $p = 50;
    }
} else {
    $p = 50;
}
 
if (defined($q->param('m'))) {
    $m = $q->param('m');
    $m = ($m =~ /^(\d)$/) ? $m : 0;
    if ($m < 0 || $m > 4) { $m = 0; };
} else {
    $m = 0;
}  

if (defined($q->param('r'))) {
    $r = $q->param('r');
    if ($r =~ /^(\d+)$/) {
        $r = $1;
    } else {
        $r = $time;
    }
} else {
    $r = $time;
}

if (defined($q->param('gens'))) {
    $g = $q->param('gens');
}
if (defined($q->param('width'))) {
    $w = $q->param('width');
}
if (defined($q->param('s'))) {
    $s = $q->param('s');
}

# Color args.

if (defined($q->param('br'))) {
    $br = $q->param('br');
    $br = ( $br =~ /^\s*(\d+)\s*$/) ? $1 : 0;
    if( $br < 0 || $br > 255) { $br = 0; };
} else {
    $br = 0;
}
if (defined($q->param('bg'))) {
    $bg = $q->param('bg');
    $bg = ( $bg =~ /^\s*(\d+)\s*$/) ? $1 : 0;
    if( $bg < 0 || $bg > 255) { $bg = 0; };
} else {
    $bg = 0;
}
if (defined($q->param('bb'))) {
    $bb = $q->param('bb');
    $bb = ( $bb =~ /^\s*(\d+)\s*$/) ? $1 : 0;
    if( $bb < 0 || $bb > 255) { $bb = 0; };
} else {
    $bb = 0;
}
if (defined($q->param('wr'))) {
    $wr = $q->param('wr');
    $wr = ( $wr =~ /^\s*(\d+)\s*$/) ? $1 : 0;
    if( $wr < 0 || $wg > 255) { $wr = 0; };
} else {
    $wr = 0;
}
if (defined($q->param('wg'))) {
    $wg = $q->param('wg');
    $wg = ( $wg =~ /^\s*(\d+)\s*$/) ? $1 : 0;
    if( $wg < 0 || $wg > 255) { $wg = 0; };
} else {
    $wg = 0;
}
if (defined($q->param('wb'))) {
    $wb = $q->param('wb');
    $wb = ( $wb =~ /^\s*(\d+)\s*$/) ? $1 : 255;
    if( $wb < 0 || $wb > 255) { $wb = 255; };
} else {
    $wb = 255;
}

$qstr = "?r=$r&gens=$g&width=$w&m=$m&p=$p&s=$s&br=$br&bg=$bg&bb=$bb".
        "&wr=$wr&wg=$wg&wb=$wb";

print <<EOH;
<HTML><HEAD><TITLE>$r</TITLE></HEAD>
<BODY BACKGROUND="jdmca.cgi$qstr">
</BODY>
</HTML>
EOH

