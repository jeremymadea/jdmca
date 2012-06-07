#!/usr/bin/perl
use CGI;
$q = new CGI;

print "Content-type: text/html\n\n";

sub ca_image_link {
    my $r = shift;
    my $g = shift;
    my $w = shift;
    my $m = shift;
    my $p = shift;
    my $s = shift;
    my $br = shift;
    my $bg = shift;
    my $bb = shift;
    my $wr = shift;
    my $wg = shift;
    my $wb = shift;

    return '<A HREF="ca_explorer.cgi'.
           "?r=$r&gens=$g&width=$w&m=$m&p=$p&s=$s&br=$br&bg=$bg&bb=$bb".
           "&wr=$wr&wg=$wg&wb=$wb".'">'.
           '<IMG BORDER=0 '."WIDTH=$w HEIGHT=$g ".
           'SRC="jdmca.cgi'."?r=$r&width=$w&gens=$g&m=$m".
           "&p=$p&s=$s&br=$br&bg=$bg&bb=$bb&wr=$wr&wg=$wg&wb=$wb".'"></A>';
}

sub flipbit {
    my $n = shift;
    my $b = shift;

    $bit = ($n >> $b) % 2;
    if ($bit) {
        $num = $n - (2**$b);
    } else {
        $num = $n + (2**$b);
    }
    return sprintf("%lu",$num);
}

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

print <<EOH;
<HTML>
<HEAD><TITLE>Jeremy's CA Explorer (and background generator)</TITLE></HEAD>
</HTML>
<BODY BGCOLOR=black
      LINK=orchid
      VLINK=darkorchid
      TEXT=white> 
<CENTER>
<H1>Jeremy's CA Explorer (and background generator.)</H1>

<TABLE BORDER=5 CELLPADDING=0 CELLSPACING=0>
<TR>
EOH

foreach $i (0..31) {
    $small_ca[$i] = '<TD ALIGN=center VALIGN=center>'.
                    ca_image_link(flipbit($r,$i),50, 50, $m, $p, $s,
                                  $br, $bg, $bb, $wr, $wg, $wb)."</TD>\n";
}

foreach $i (0..7) {
    print $small_ca[$i];
}
print "</TR>\n<TR>\n";
print $small_ca[8];
print $small_ca[9];
print "<TD ALIGN=center COLSPAN=4 ROWSPAN=4>".
                    '<A HREF="ca_deep.cgi'.
                    "?r=$r&gens=200&width=200&m=$m&p=$p&s=$s".
                    "&br=$br&bg=$bg&bb=$bb&wr=$wr&wg=$wg&wb=$wb".'">'.
                    '<IMG BORDER=0 WIDTH=200 HEIGHT=200 SRC="'.
                    "jdmca.cgi?r=$r&gens=200&width=200w&m=$m&p=$p&s=$s".
                    "&br=$br&bg=$bg&bb=$bb&wr=$wr&wg=$wg&wb=$wb".'"></A></TD>';

foreach $i (10..31) {
    print $small_ca[$i];
    if ( ($i == 11) ||
         ($i == 15) ||
         ($i == 19) ||
         ($i == 23) ||
         ($i == 31) ) {
        print "</TR>\n".
              "<TR>\n";
    }
}

print <<EOF;
</TR>
</TABLE>
</CENTER>
<FORM ACTION="ca_explorer.cgi" METHOD=GET>
<INPUT TYPE="hidden" NAME="r" VALUE="$r">
<CENTER>
Click on the large image above to play with it some more.<BR>
Click on one of the smaller images above to try a different RuleSet.<BR>
</CENTER>
<HR>
<CENTER>
<A HREF="ca_deep.cgi?$qstr">Microscope</A> &nbsp &nbsp
<A HREF="ca_instruct.html">Instructions</A> &nbsp &nbsp
<A HREF="ca_credits.html">Credits</A> &nbsp &nbsp
<A HREF="ca_about.html">About This CA</A> &nbsp &nbsp
<A HREF="ca_faves.html">My Favorites</A> &nbsp &nbsp
<A HREF="ca_links.html">CA Links</A> &nbsp &nbsp
<A HREF="ca_main.html">Main Site</A> &nbsp &nbsp
<BR>
</CENTER>
<HR>

<BR>
Dead Cell Color: &nbsp 
<FONT COLOR="red">Red:</FONT>
<INPUT TYPE="text" SIZE=3 MAXLENGTH=3 NAME="br" VALUE="$br">
<FONT COLOR="green">Green:</FONT>
<INPUT TYPE="text" SIZE=3 MAXLENGTH=3 NAME="bg" VALUE="$bg">
<FONT COLOR="blue">Blue:</FONT>
<INPUT TYPE="text" SIZE=3 MAXLENGTH=3 NAME="bb" VALUE="$bb"> &nbsp

Percentage of live cells in first row: &nbsp 
<INPUT TYPE="text" SIZE=3 MAXLENGTH=3 NAME="p" VALUE="$p"><BR>

Live Cell Color: &nbsp &nbsp
<FONT COLOR="red">Red:</FONT>
<INPUT TYPE="text" SIZE=3 MAXLENGTH=3 NAME="wr" VALUE="$wr">
<FONT COLOR="green">Green:</FONT>
<INPUT TYPE="text" SIZE=3 MAXLENGTH=3 NAME="wg" VALUE="$wg">
<FONT COLOR="blue">Blue:</FONT>
<INPUT TYPE="text" SIZE=3 MAXLENGTH=3 NAME="wb" VALUE="$wb">
&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp
<INPUT TYPE="submit" VALUE="Change">
</FORM>
</BODY>
</HTML>
EOF
