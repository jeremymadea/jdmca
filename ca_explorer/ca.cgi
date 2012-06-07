#!/usr/bin/perl
use CGI;
$q = new CGI;

print "Pragma: no-cache\n";
print "Content-type: image/gif\n\n";

$time = time;

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

if ($q->param('s')) {
    $s = $q->param('s');
    if ($s =~ /^(\d+)$/) {
        $s = $1;
    } else {
        $s = 100;
    }
} else {
    $s = 100;
}

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

if ($q->param('c')) {
    $c = $q->param('c');
    if ($c =~ /^([A-Fa-f0-9]+)$/) {
        $c = $1;
    } else {
        $c = 'ffffff';
    }
} else {
    $c = 'ffffff';
}

print `./jdmca -p $p -x $s -y $s -w $c -b 000000 -r $r`;
