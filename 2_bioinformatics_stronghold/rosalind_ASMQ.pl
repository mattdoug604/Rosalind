#!/usr/bin/perl

=begin comment
Rosalind: Bioinformatics Stronghold
Problem: Assessing Assembly Quality with N50 and N75
URL: http://rosalind.info/problems/asmq/

Given: A collection of at most 1000 DNA strings (whose combined length does
not exceed 50 kbp).

Return: N50 and N75 for this collection of strings.
=end comment
=cut

use strict; use warnings;
 use POSIX;

# Read in a number of DNA sequences (one per line)
my $file = 'problem_datasets/rosalind_asmq.txt';
open(my $fh, $file) or die "Could not open $file\n";;
my @seqs = ();
while(<$fh>) {
  chomp $_;
  push @seqs, $_;
}

#Create a sorted list containing n copies of an integer, n; where n is the
#length of each given string in a list.
my @lenlist = (0);
foreach my $i (@seqs) {
  my @l = (length($i)) x length($i);
  push @lenlist, @l;
}
@lenlist = sort { $a <=> $b } @lenlist;

sub Nxx {
  # Take the mean of the two middle elements if there are an even number of
  # elements. Otherwise, take the middle element.
  my $n = 100 / (100 - shift);
  my $medianpos = $#lenlist / $n;
  if($#lenlist % 2 == 0) {
    return $lenlist[$medianpos] + $lenlist[$medianpos-1] / $n;
  } else {
    return $lenlist[$medianpos];
  }
}

# Output answer
print Nxx(50) . " " . Nxx(75) . "\n";
