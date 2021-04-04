#!/usr/bin/env python3

"""
Rosalind: Bioinformatics Stronghold
Problem: Constructing a De Bruijn Graph
URL: http://rosalind.info/problems/dbru/

Given: A collection of up to 1000 DNA strings of equal length (not exceeding 
50 bp) corresponding to a set S of (k+1)-mers.

Return: The adjacency list corresponding to the de Bruijn graph corresponding 
to S ∪ Src.
"""

from collections import defaultdict

from rosalind_utils import reverse_complement as rc


def de_bruijn(seq_list):
    # Add the reverse complements of the k+1-mers.
    seq_list = list(set(seq_list + [rc(i) for i in seq_list]))

    # Function to split a string into two kmers.
    kmers_in_seq = lambda seq: (seq[:-1], seq[1:])

    # Find which sequences each kmer occurs in.
    kmers = defaultdict(list)
    for seq in seq_list:
        for k in kmers_in_seq(seq):
            kmers[k].append(seq)

    # Find unique, adjacent kmers in the De Bruijn tree.
    adjacency = defaultdict(set)
    for kmer, seqs in kmers.items():
        for seq in seqs:
            for k in kmers_in_seq(seq):
                if kmer[1:] == k[:-1]:
                    adjacency[kmer].add(k)

    return adjacency


def main():
    # Read a list of equal length kmers.
    with open("problem_datasets/rosalind_dbru.txt", "r") as infile:
        s = infile.read().strip().split("\n")

    # Get a dictionary of adjacent kmers.
    answer = de_bruijn(s)

    # Output the answer as pairs of adjacencies.
    with open("output/rosalind_dbru_out.txt", "w") as outfile:
        for i in answer:
            for j in answer[i]:
                outfile.write("(" + i + ", " + j + ")\n")


if __name__ == "__main__":
    main()
