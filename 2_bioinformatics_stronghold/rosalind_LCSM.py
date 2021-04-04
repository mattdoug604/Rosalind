#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Finding a Shared Motif
URL: http://rosalind.info/problems/lcsm/

Given: A collection of k (k <= 100) DNA strings of length at most 1 kbp each in
FASTA format.
Return: A longest common substring of the collection. (If multiple solutions
exist, you may return any single solution.)
"""

from rosalind_utils import parse_fasta


def longest_motif(seq_list):
    """Finds the longest common substring (motif) from all the sequences.
    Note: the script only returns the *first* motif it finds
    """
    first_seq = min(seq_list, key=len)
    k = len(first_seq)

    for i in range(k, 1, -1):
        for j in range(k - i + 1):
            motif = first_seq[j : j + i]
            found = True

            for seq in seq_list:
                s = seq.find(motif)
                if s == -1:
                    found = False
                    break

            if found == True:
                return motif


def main():
    sequences = parse_fasta("problem_datasets/rosalind_lcsm.txt")

    answer = longest_motif(sequences)

    if answer != None:
        print(answer)
    else:
        print("No common substring found.")


if __name__ == "__main__":
    main()
