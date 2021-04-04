#!/usr/bin/env perl

=begin comment
Rosalind: Bioinformatics Stronghold
Problem: Consensus and Profile
URL: http://rosalind.info/problems/cons/

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp)
in FASTA format.
Return: A consensus string and profile profile for the collection. (If several
possible consensus strings exist, then you may return any one of them.)
=end comment
=cut

use strict; use warnings;
use List::Util qw(reduce);

# Read in the FASTA sequences
my @seqs = parse_fasta('problem_datasets/rosalind_cons.txt');
# Length of the first sequence (assuming all sequences are the same length)
my $l = length($seqs[0]);
# Four arrays which will make the profile matrix
my @A = (0)x$l;
my @C = (0)x$l;
my @G = (0)x$l;
my @T = (0)x$l;
# Consensus sequence
my @consensus = ("")x$l;

# Create profile matrix and consensus sequence
for(my $i=0; $i<$l; $i++) {
  # Count the number of occurances of each nucleotide at each position
  foreach (@seqs) {
    my $nt = substr($_, $i, 1);
    if($nt eq "A") {
      $A[$i] += 1;
    } elsif($nt eq "C") {
      $C[$i] += 1;
    } elsif($nt eq "G") {
      $G[$i] += 1;
    } elsif($nt eq "T") {
      $T[$i] += 1;
    }
  }
  # Find the most common nucleotide at each position. If multiple nucleotides
  # occur the same number of times, just use the first in the list.
  my %occurances = ( A=>$A[$i], C=>$C[$i], G=>$G[$i], T=>$T[$i] );
  my $most_common = List::Util::reduce { $occurances{$b} > $occurances{$a} ? $b : $a } keys %occurances;
  print $most_common;
}

# Output consensus sequence and profile matrix in the proper format
print @consensus, "\n";   #TCTCAATACCGTCCCCCGGTAAGTATGGACTCTGGAATTTAG...
print "A: @A\n";          #A: 2 2 3 1 3 4 1 4 1 3 2 2 2 1 3 0 2 1 2 1...
print "C: @C\n";          #C: 2 3 0 7 2 0 3 2 5 4 1 1 4 5 4 4 5 3 2 3...
print "G: @G\n";          #G: 2 3 3 1 3 3 2 1 4 3 6 3 0 0 2 4 2 5 4 2...
print "T: @T\n";          #T: 4 2 4 1 2 3 4 3 0 0 1 4 4 4 1 2 1 1 2 4...

sub parse_fasta {
  # Read each sequence into a list (sequence IDs are not recorded)
  open(my $fh, shift) or die "Could not open file!\n";

  my @seqs = ();
  while(<$fh>) {
    chomp $_;
    if($_ =~ /^>/) {
      push @seqs, "";
    } else {
      $seqs[-1] .= $_;
    }
  }

  return @seqs;
}
