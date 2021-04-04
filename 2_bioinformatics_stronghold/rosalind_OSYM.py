#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Isolating Symbols in Alignments
URL: http://rosalind.info/problems/osym/

Given: Two DNA strings s and t in FASTA format, each having length at most 
1000 bp.

Return: The maximum alignment score of a global alignment of s and t, followed 
by the sum of all elements of the matrix M corresponding to s and t that was 
defined above. Apply the mismatch score introduced in “Finding a Motif with 
Modifications”.
"""
from os.path import dirname, join

from utils import parse_fasta

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_osym.txt")


def global_alignment(s, t):
    # Initialize the score matrix.
    S = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]

    # Each cell in the first row and column recieves a gap penalty.
    for i in range(1, len(s) + 1):
        S[i][0] = -i
    for j in range(1, len(t) + 1):
        S[0][j] = -j

    # Fill in the score matrix.
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if i == len(s) + 1 and j == len(t) + 1:
                S[i][j] = S[i - 1][j - 1] + [-1, 1][s[i - 1] == t[j - 1]]
            else:
                S[i][j] = max(
                    [
                        S[i - 1][j - 1] + [1, -1][s[i - 1] != t[j - 1]],
                        S[i - 1][j] - 1,
                        S[i][j - 1] - 1,
                    ]
                )

    # Return the alignment matrix
    return S


def align_to_symbols(s, t):
    # Will be used to hold the sum of the alignment scores.
    total = 0
    # Initialize the best score as some arbitrary small value.
    best = -(len(s) + len(t))

    # Create one alignment matrix of s and t, and one of s and t reversed.
    prefix_matrix = global_alignment(s, t)
    suffix_matrix = global_alignment(s[::-1], t[::-1])

    # The alignment score of two sequences with two explicitly aligned sybols
    # is the sum of the alignment scores of the two symbols, the alignment
    # scores of preceeding part of the sequences, and the following part of the
    # sequences.
    # Example:
    #     s -> ATAG  A  --TA
    #     t -> AC--  A  GGTA
    # score ->  -2 + 1 + 0  = -1
    for i in range(len(s)):
        for j in range(len(t)):
            score = sum(
                (
                    prefix_matrix[i][j],
                    [-1, 1][s[i] == t[j]],
                    suffix_matrix[len(s) - 1 - i][len(t) - 1 - j],
                )
            )

            total += score

            # Keep track of the highest score. Alternatively, the highest
            # score can be found in the last cell of a matrix of each
            # alignment.
            if score > best:
                best = score

    # Return the highest score, and the sum of all the scores.
    return best, total


def main():
    # Get the sequences from the .txt file.
    s, t = parse_fasta(INPUT_FILE)

    # Compute the maximum alignment score, and the sum of all alignment scores.
    print("\n".join(map(str, align_to_symbols(s, t))))


if __name__ == "__main__":
    main()
