#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Finding a Spliced Motif
URL: http://rosalind.info/problems/sseq/

Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.
Return: One collection of indices of s in which the symbols of t appear as a
subsequence of s. If multiple solutions exist, you may return any one.
"""

from utils import parse_fasta


def find_subsequence(s, t):
    """Finds the indices of the symbols in 't' that appear as a subsequence
    of 's'. The symbols in 't' are a subsequence if the appear in the same
    order within 's'.
    """
    symbols = list(t)

    index = []
    i = 0
    for pos, nt in enumerate(s):
        if nt == symbols[i]:
            index.append(str(pos + 1))
            if i < len(symbols) - 1:
                i += 1
            else:
                break

    return index


def main():
    """The input file for this problem contains two FASTA sequences, which can
    be split into seperate sequences based on the position of the header
    lines.
    """
    s, t = parse_fasta("problem_datasets/rosalind_sseq.txt")

    pos = find_subsequence(s, t)
    print(" ".join(pos))


if __name__ == "__main__":
    main()
