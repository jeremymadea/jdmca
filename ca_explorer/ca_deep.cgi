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
    $g = ( $g =~ /^\s*(\d+)\s*$/) ? $1 : 0;
    if( $g < 5 || $g > 2048) { $g = 200; };
}
if (defined($q->param('width'))) {
    $w = $q->param('width');
    $w = ( $w =~ /^\s*(\d+)\s*$/) ? $1 : 0;
    if( $w < 5 || $w > 2048) { $w = 200; };

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
<HTML><HEAD><TITLE>CA Microscope: A closer look at $r.</TITLE></HEAD>
<BODY BGCOLOR=black
      TEXT=white
      LINK=orchid
      VLINK=darkorchid>
<CENTER>
<H1>CA Microscope: (RuleSet: $r)</H1>
<TABLE BORDER=5>
<TR>
<TD><A HREF="ca_back.cgi$qstr"><IMG BORDER=0 SRC="jdmca.cgi$qstr">
</TR>
</TABLE>
</CENTER>
<FORM ACTION="ca_deep.cgi" METHOD=GET>
<INPUT TYPE="hidden" NAME="r" VALUE="$r">
<CENTER>
To see this image tiled as a background, click on it.<BR> You may save a copy of it
for yourself in the usual way you save images with your browser.<BR>
</CENTER>
<HR>
<CENTER>
<A HREF="ca_explorer.cgi$qstr">Explorer</A> &nbsp &nbsp
<A HREF="ca_instruct.html">Instructions</A> &nbsp &nbsp
<A HREF="ca_credits.html">Credits</A> &nbsp &nbsp
<A HREF="ca_about.html">About This CA</A> &nbsp &nbsp
<A HREF="ca_faves.html">My Favorites</A> &nbsp &nbsp
<A HREF="ca_links.html">CA Links</A> &nbsp &nbsp
<A HREF="ca_main.html">Main Site</A> &nbsp &nbsp
<BR>
</CENTER>
<HR>
Width:<INPUT TYPE="text" SIZE=4 MAXLENGTH=4 NAME="width" VALUE="$w"> &nbsp
Generations: <INPUT TYPE="text" SIZE=4 MAXLENGTH=4 NAME="gens" VALUE="$g"> &nbsp

% alive at start: &nbsp 
<INPUT TYPE="text" SIZE=3 MAXLENGTH=3 NAME="p" VALUE="$p"> &nbsp
First row fill mode: &nbsp 
<INPUT TYPE="text" SIZE=1 MAXLENGTH=1 NAME="m" VALUE="$m"><BR>

Dead Cell Color: &nbsp 
<FONT COLOR="red">Red:</FONT>
<INPUT TYPE="text" SIZE=3 MAXLENGTH=3 NAME="br" VALUE="$br">
<FONT COLOR="green">Green:</FONT>
<INPUT TYPE="text" SIZE=3 MAXLENGTH=3 NAME="bg" VALUE="$bg">
<FONT COLOR="blue">Blue:</FONT>
<INPUT TYPE="text" SIZE=3 MAXLENGTH=3 NAME="bb" VALUE="$bb"> &nbsp
<BR>

Live Cell Color: &nbsp &nbsp
<FONT COLOR="red">Red:</FONT>
<INPUT TYPE="text" SIZE=3 MAXLENGTH=3 NAME="wr" VALUE="$wr">
<FONT COLOR="green">Green:</FONT>
<INPUT TYPE="text" SIZE=3 MAXLENGTH=3 NAME="wg" VALUE="$wg">
<FONT COLOR="blue">Blue:</FONT>
<INPUT TYPE="text" SIZE=3 MAXLENGTH=3 NAME="wb" VALUE="$wb"> <BR>

Start row: <BR>
<INPUT TYPE="text" SIZE=80 MAXLENGTH=400 NAME="s" VALUE="$s"><BR>
<CENTER>
<INPUT TYPE="submit" VALUE="Change">
</CENTER>
</FORM>
</BODY>
</HTML>
EOH

