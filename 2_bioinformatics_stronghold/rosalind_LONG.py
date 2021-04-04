#!/usr/bin/env python3

'''
Rosalind: Bioinformatics Stronghold
Problem: Genome Assembly as Shortest Superstring
URL: http://rosalind.info/problems/long/

Given: At most 50 DNA strings whose length does not exceed 1 kbp in FASTA 
format (which represent reads deriving from the same strand of a single linear
chromosome). The dataset is guaranteed to satisfy the following condition:
there exists a unique way to reconstruct the entire chromosome from these 
reads by gluing together pairs of reads that overlap by more than half their 
length.

Return: A shortest superstring containing all the given strings (thus
corresponding to a reconstructed chromosome).
'''

from rosalind_utils import parse_fasta

def match_seq(seq, seq_list):
    ''' Starting with a length 1 less than the total length of a given 
        sequence, look for iteratively smaller areas of overlap with the other 
        sequences (down to just over half the length of the sequence). Stops 
        at the first found case of overlap and returns a superstring made by 
        combining the two sequences.
    '''    
    half = int(len(seq)/2)
    
    for i in range(len(seq)-1, half, -1):
        overlap = seq[len(seq)-i:]

        for seq2 in seq_list:
            if seq2 != seq:
                if seq2[:i] == overlap:
                    return seq[:len(seq)-i] + seq2


def shortest_contig(seq_list):
    ''' Iteratively create overlapping superstrings until only one is left 
        (i.e. the shortest contig).
    '''
    while len(seq_list) > 1:
        new_list = []
        for seq in seq_list:
            match = match_seq(seq, seq_list)
            if match != None:
                new_list.append(match)
    
        seq_list = new_list

    return seq_list[0]

    
def main():
    # Extract sequences from a fasta file.
    seqs = parse_fasta('problem_datasets/rosalind_long.txt')
    
    # Find the shortest superstring.
    answer = shortest_contig(seqs)
    
    # Write the answer.
    open('output/rosalind_long_out.txt', 'w').write(answer)

    # Optional: Print the length of the superstring.
    print('Shortest superstring is %i nucleotides long.' % len(answer))


if __name__ == '__main__':
    main()
