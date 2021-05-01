#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Consensus and Profile
URL: http://rosalind.info/problems/cons/

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp)
in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several
possible consensus strings exist, then you may return any one of them.)
"""
from os.path import dirname, join

from utils import parse_fasta

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_cons.txt")


def profile_matrix(seqs):
    """Generate a profile matrix from a list of DNA sequences."""
    length = len(min(seqs, key=len))  # in case the strings are different lengths
    matrix = [[0 for x in range(4)] for y in range(length)]
    letters = {"A": 0, "C": 1, "G": 2, "T": 3}

    for i in range(length):
        for string in seqs:
            s = string[i]
            if s in letters:
                matrix[i][letters[s]] += 1

    return matrix


def consensus_seq(profile):
    """Determine the consensus sequence from a given profile matrix."""
    consensus = ""
    letter = ["A", "C", "G", "T"]

    for i in range(len(profile)):
        nt = profile[i].index(max(profile[i]))
        consensus += letter[nt]

    return consensus


def format_profile(profile):
    """A generator that outputs the profile matrix in a readable format."""
    prefix = ["A", "C", "G", "T"]

    for i in range(4):
        line = prefix[i] + ": "
        for j in range(len(profile)):
            line += str(profile[j][i]) + " "

        yield line


def main():
    sequences = parse_fasta(INPUT_FILE)
    profile = profile_matrix(sequences)
    consensus = consensus_seq(profile)

    print(consensus)
    for line in format_profile(profile):
        print(line)


if __name__ == "__main__":
    main()
