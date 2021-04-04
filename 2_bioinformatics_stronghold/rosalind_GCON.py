#!/usr/bin/env python
"""
Rosalind: Bioinformatics Stronghold
Problem: Global Alignment with Constant Gap Penalty
URL: http://rosalind.info/problems/gcon/

Given: Two protein strings s and t in FASTA format (each of length at most 1000
aa).
Return: The maximum alignment score between s and t. Use:
    - The BLOSUM62 scoring matrix.
    - Constant gap penalty equal to 5.

EXAMPLE INPUT:
>Rosalind_79
PLEASANTLY
>Rosalind_41
MEANLY

EXAMPLE OUTPUT:
13
"""

from utils import BLOSUM62, match_score, parse_fasta


def global_align(s, t, matrix, gap):

    # Score of best alignment ending with a match or mismatch.
    M = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
    # Initialize the gap matrices with an arbitrarily small number.
    # Score of best alignment ending with a space in X.
    X = [[-9999 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
    # Score of best alignment ending with a space in Y.
    Y = [[-9999 for j in range(len(t) + 1)] for i in range(len(s) + 1)]

    for i in range(1, len(s) + 1):
        M[i][0] = gap
    for j in range(1, len(t) + 1):
        M[0][j] = gap

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            X[i][j] = max([M[i - 1][j] + gap, X[i - 1][j]])
            Y[i][j] = max([M[i][j - 1] + gap, Y[i][j - 1]])
            M[i][j] = max(
                [M[i - 1][j - 1] + match_score(matrix, s[i - 1], t[j - 1]), X[i][j], Y[i][j]]
            )

    # The max possible score is found at the bottom-right corner of the matrix.
    return M[-1][-1]


def main():
    s, t = parse_fasta("problem_datasets/rosalind_gcon.txt")
    max_score = global_align(s, t, BLOSUM62(), -5)

    print(max_score)


if __name__ == "__main__":
    main()
