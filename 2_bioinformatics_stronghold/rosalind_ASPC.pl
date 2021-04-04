#!/usr/bin/env perl

# UNFINISHED

=begin comment
Rosalind: Bioinformatics Stronghold
Problem: Introduction to Alternative Splicing
URL: http://rosalind.info/problems/aspc/

Given: Positive integers n and m with 0 <= m <= n <= 2000.
Return: The sum of combinations C(n,k) for all k satisfying m <= k <= n, modulo
1,000,000.

EXAMPLE INPUT:
6 3

EXAMPLE OUTPUT:
42
=end comment
=cut

use strict; use warnings;
use Math::Counting ':big';

sub factorial {
  my ($n, $m) = @_;
  my $sum = 0;
  for(my $k=$m; $k<$n+1; $k++) { $sum += bcomb($n, $k); }
  return $sum;
}

# Read in a variables "n" and "m" seperated by spaces
my $file = 'problem_datasets/rosalind_aspc.txt';
open my $fh, '<', $file or die "Could not open $file\n";
my $line = <$fh>;
my ($n, $m) = split / /, $line;
my $out = factorial($n, $m);
print $out % 1000000 . "\n";
