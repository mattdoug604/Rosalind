#!/usr/bin/perl

=begin comment
Rosalind: Bioinformatics Stronghold
Problem: Counting Disease Carriers
URL: http://rosalind.info/problems/afrq/

Given: An array A for which A[k] represents the proportion of homozygous
recessive individuals for the k-th Mendelian factor in a diploid population.
Assume that the population is in genetic equilibrium for all factors.

Return: An array B having the same length as A in which B[k] represents the
probability that a randomly selected individual carries at least one copy of
the recessive allele for the k-th factor.
=end comment
=cut

use strict; use warnings;

# Read in a space-seperated list of floats to an array
my $file = 'problem_datasets/rosalind_afrq.txt';
open(my $fh, $file) or die "Could not open $file\n";
my @array = ();
while(<$fh>) {
  chomp $_;
  push @array, split / /, $_;
}

# Calculate the probability of each value in the array
my @probs = ();
foreach my $val (@array) {
  my $p = sqrt($val);
  my $q = 1 - $p;
  my $ans = (2 * $p * $q) + $val;
  push @probs, $ans;
}

# Print the answers rounded to 3 decimals places
foreach (@probs) {
  printf("%.3f ", $_);
}
