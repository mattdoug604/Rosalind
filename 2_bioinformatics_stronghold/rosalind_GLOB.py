#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Global Alignment with Scoring Matrix
URL: http://rosalind.info/problems/glob/

Given: Two protein strings s and t in FASTA format (each of length at most 
1000 aa).

Return: The maximum alignment score between s and t. Use:
        - The BLOSUM62 scoring matrix.
        - Linear gap penalty equal to 5 (i.e., a cost of -5 is assessed for 
          each gap symbol).
 
EXAMPLE INPUT:
>Rosalind_67
PLEASANTLY
>Rosalind_17
MEANLY

EXAMPLE OUTPUT:
8
"""

from rosalind_utils import BLOSUM62, match_score, parse_fasta


def global_align(s, t, scores, gap):
    # Initialize the similarity matrix.
    S = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]

    # Each cell in the first row and column recieves a gap penalty.
    for i in range(1, len(s) + 1):
        S[i][0] = i * gap
    for j in range(1, len(t) + 1):
        S[0][j] = j * gap

    # Fill in the similarity matrix.
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            S[i][j] = max(
                [
                    S[i - 1][j - 1] + match_score(scores, s[i - 1], t[j - 1]),
                    S[i - 1][j] + gap,
                    S[i][j - 1] + gap,
                ]
            )

    # The max possible score is the last cell of the similarity matrix.
    return S[-1][-1]


def main():
    s, t = parse_fasta("problem_datasets/rosalind_glob.txt")
    max_score = global_align(s, t, BLOSUM62(), -5)

    print(max_score)


if __name__ == "__main__":
    main()
