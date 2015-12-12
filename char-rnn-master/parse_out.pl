#!/usr/bin/perl
use strict;
use warnings;

my $file1 = "out_data.txt";
open (my $csvfile1, "<", $file1) or die $!;
open (FILE, ">", "out_data2.txt") or die $!;

while (my $row = <$csvfile1>) {
$row =~ s/[^a-zA-Z0-9 _-]//g;
	print FILE $row."

";
}

close $csvfile1;
close FILE;
