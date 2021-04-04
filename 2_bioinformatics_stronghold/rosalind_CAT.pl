#!/usr/bin/env perl

=begin comment
Rosalind: Bioinformatics Stronghold
Problem: Catalan Numbers and RNA Secondary Structures
URL: http://rosalind.info/problems/cat/

Given: An RNA string s having the same number of occurrences of 'A' as
'U' and the same number of occurrences of 'C' as 'G'. The length of the
string is at most 300 bp.
Return: The total number of noncrossing perfect matchings of basepair
edges in the bonding graph of s, modulo 1,000,000.

EXAMPLE INPUT:
>Rosalind_57
AUAU

EXAMPLE OUTPUT:
2
=end comment
=cut

use strict; use warnings;
use bigint;

# Possible basepair matches
my %bases = ('A'=>'U', 'U'=>'A', 'C'=>'G', 'G'=>'C');

# Retrieve sequence from FASTA file
my $seq = read_fasta('problem_datasets/rosalind_cat.txt');
#my $seq = 'AUAU';

# Create a 2D array to store the number of matches, of size x^2 where
# x = length of sequence + 1
my @pairs = build_matrix(length($seq)+1);

# Count all possible matches
my $count = count_matchings(0, length($seq)-1);

# Output the answer
print $count % 1000000 . "\n";

sub read_fasta {
	my $file = shift;
	open(my $fh, $file) or die "Could not open $file\n";

	my $seq = '';

	my $header = <$fh>;	# skip FASTA header
	while(<$fh>) {
		chomp $_;
		$seq .= $_;
	}

	return $seq;
}

sub build_matrix {
	my $length = shift;

	my @pairs = ();
	for (my $i=0; $i<$length; $i++) {
		push(@pairs, [(-1) x $length])
	}

	return @pairs
}

sub count_matchings {
	my ($i, $j) = @_;
	my $result = 0;

	if($pairs[$i][$j] != -1) {
		return $pairs[$i][$j];
	}

	if($i > $j) {
		$result = 1;
	} else {
		for(my $k=$i+1; $k<$j+1; $k+=2) {
			if(substr($seq, $k, 1) eq $bases{substr($seq, $i, 1)}) {
				$result += count_matchings($i+1, $k-1) * count_matchings($k+1, $j);
			}
		}
	}

	$pairs[$i][$j] = $result;
	return $result;
}
