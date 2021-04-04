#!/usr/bin/env python3

"""
Rosalind: Bioinformatics Stronghold
Problem: Genome Assembly with Perfect Coverage
URL: http://rosalind.info/problems/pcov/

Given: A collection of (error-free) DNA kk-mers (k≤50) taken from the same 
strand of a circular chromosome. In this dataset, all kk-mers from this strand 
of the chromosome are present, and their de Bruijn graph consists of exactly 
one simple cycle.

Return: A cyclic superstring of minimal length containing the reads (thus 
corresponding to a candidate cyclic chromosome).
"""


def adjacency_list(seq_list):
    # Function to split a string into two kmers.
    kmers_in_seq = lambda seq: (seq[:-1], seq[1:])

    # Find which sequences each kmer occurs in.
    kmers = {}
    for seq in seq_list:
        for k in kmers_in_seq(seq):
            if k in kmers:
                kmers[k].append(seq)
            else:
                kmers[k] = [seq]

    # Find unique, adjacent kmers in the De Bruijn tree.
    adjacency = {}
    for kmer, seqs in kmers.items():
        for seq in seqs:
            for k in kmers_in_seq(seq):
                if kmer[1:] == k[:-1]:
                    adjacency[kmer] = k

    return adjacency


def cyclic_superstring(dna):
    # Get the adjacecny list of the collection of strings.
    adj = adjacency_list(dna)

    # Start with whatever element is first in the adjacency list...
    first = next(iter(adj.keys()))
    superstring = first

    # That element is adjacent to another element...
    prev = adj[superstring]

    # Loop through each element, connecting the adjacent kmers together as we
    # go. Stop once we loop back to the kmer we started with.
    while prev != first:
        superstring += prev[-1]
        prev = adj[prev]

    # Start in the middle of the superstring, look for progressively smaller
    # substrings until you find one that overlaps with the beginning of the
    # superstring. That is where the superstring circularizes.
    i = len(superstring) // 2
    while i < len(superstring):
        if superstring[i:] == superstring[: len(superstring) - i]:
            superstring = superstring[:i]
            break
        i += 1

    return superstring


def main():
    with open("problem_datasets/rosalind_pcov.txt", "r") as infile:
        dna = infile.read().strip().split("\n")

    with open("output/rosalind_pcov_out.txt", "w") as outfile:
        outfile.write(cyclic_superstring(dna))


if __name__ == "__main__":
    main()
