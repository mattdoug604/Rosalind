#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Finding a Shared Spliced Motif
URL: http://rosalind.info/problems/lcsq/

Given: Two DNA strings s and t (each having length at most 1 kbp) in FASTA
format.
Return: A longest common subsequence of s and t. (If more than one solution
exists, you may return any one.)
 
EXAMPLE INPUT:
>Rosalind_23
AACCTTGG
>Rosalind_64
ACACTGTGA

EXAMPLE OUTPUT:
AACTGG
"""
from os.path import dirname, join

from utils import parse_fasta

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_lcsq.txt")


def build_matrix(s, t, m, n):
    d = [[[] for x in range(n + 1)] for y in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                d[i][j] = 0
            elif s[i - 1] == t[j - 1]:
                d[i][j] = d[i - 1][j - 1] + 1
            else:
                d[i][j] = max(d[i - 1][j], d[i][j - 1])

    return d


def longest_sub(s, t):
    i = len(s)
    j = len(t)
    table = build_matrix(s, t, i, j)

    seq = ""
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:
            seq = s[i - 1] + seq
            i -= 1
            j -= 1
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return seq


def main():
    s, t = parse_fasta(INPUT_FILE)
    seq = longest_sub(s, t)

    print(seq)

    print("The longest common subsequence is", len(seq), "bases long.")


if __name__ == "__main__":
    main()
