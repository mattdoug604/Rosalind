#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Genome Assembly Using Reads
URL: http://rosalind.info/problems/gasm/

Given: A collection S of (error-free) reads of equal length (not exceeding 
50 bp). In this dataset, for some positive integer k, the de Bruijn graph 
BkBk on Sk+1∪Srck+1 consists of exactly two directed cycles.

Return: A cyclic superstring of minimal length containing every read or its 
reverse complement.
"""

from itertools import chain

from rosalind_utils import reverse_complement as rc


def cyclic_superstring(dna):
    flatten = lambda listOfLists: chain.from_iterable(listOfLists)

    n = len(dna)
    l = len(dna[0])  # assumes all strings are the same length

    for k in range(l - 1, 1, -1):
        adj = dict(
            flatten([[(d[i : i + k], d[i + 1 : i + k + 1]) for i in range(l - k)] for d in dna])
        )
        first = kmer = next(iter(adj))
        superstring = ""

        while True:
            if kmer in adj:
                superstring += kmer[-1]
                kmer = adj.pop(kmer)
                if kmer == first:
                    return superstring
            else:
                break


def main():
    with open("problem_datasets/rosalind_gasm.txt", "r") as infile:
        dna = infile.read().strip().split("\n")
        dna = list(set(dna + [rc(i) for i in dna]))  # Add the reverse complement of each string.

    with open("output/rosalind_gasm_out.txt", "w") as outfile:
        outfile.write(cyclic_superstring(dna))


if __name__ == "__main__":
    main()
