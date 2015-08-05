#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Overlap Graphs
URL: http://rosalind.info/problems/grph/

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
Return: The adjacency list corresponding to O3. You may return edges in any order.
'''

from rosalind_utils import parse_fasta

def overlap_seqs(sequences):
    for head1, seq1 in sequences.items():
        suffix = seq1[-3:]
        for head2, seq2 in sequences.items():
            prefix = seq2[:3]
            if seq1 != seq2:
                if suffix == prefix:
                    yield(' '.join([head1, head2]))


def main():
    dataset = parse_fasta("problem_datasets/rosalind_grph.txt")
    
    with open('output/rosalind_grph_out.txt', 'w') as outfile:
        for line in overlap_seqs(dataset):
            outfile.write(line + '\n')


if __name__ == '__main__':
    main()
