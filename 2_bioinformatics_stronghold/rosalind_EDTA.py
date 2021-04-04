#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Edit Distance Alignment
URL: http://rosalind.info/problems/edta/

Given: Two protein strings s and t in FASTA format (with each string having
length at most 1000 aa).
Return: The edit distance dE(s,t) followed by two augmented strings s′ and t′
representing an optimal alignment of s and t.

EXAMPLE INPUT:
>Rosalind_43
PRETTY
>Rosalind_97
PRTTEIN

EXAMPLE OUTPUT:
4
PRETTY--
PR-TTEIN
"""
from os.path import dirname, join

from utils import parse_fasta

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_edta.txt")


def edit_dist_with_align(s, t):
    # Initialize the distance and traceback matrices with zeros.
    d = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
    traceback = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]

    # Each cell in the first row and column recieves a gap penalty (-1).
    for i in range(1, len(s) + 1):
        d[i][0] = i
    for j in range(1, len(t) + 1):
        d[0][j] = j

    # Fill in the distance and traceback matrices.
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            scores = [
                d[i - 1][j - 1] + (s[i - 1] != t[j - 1]),  # 0 = match
                d[i - 1][j] + 1,  # 1 = insertion
                d[i][j - 1] + 1,
            ]  # 2 = deletion
            d[i][j] = min(scores)
            traceback[i][j] = scores.index(d[i][j])

    # The edit distance the last cell (bottom-right) of the distance matrix.
    edit_dist = d[-1][-1]

    # Initialize the aligned strings as the input strings.
    s_align, t_align = s, t

    # traceback to the edge of the matrix starting at the bottom right.
    i, j = len(s), len(t)

    while i > 0 and j > 0:
        if traceback[i][j] == 1:
            i -= 1
            t_align = t_align[:j] + "-" + t_align[j:]
        elif traceback[i][j] == 2:
            j -= 1
            s_align = s_align[:i] + "-" + s_align[i:]
        else:
            i -= 1
            j -= 1

    # Prepend insertions/deletions if necessary.
    for dash in range(i):
        t_align = t_align[:0] + "-" + t_align[0:]
    for dash in range(j):
        s_align = s_align[:0] + "-" + s_align[0:]

    return edit_dist, s_align, t_align


def main():
    s, t = parse_fasta(INPUT_FILE)
    aligned = edit_dist_with_align(s, t)

    with open("output/rosalind_edta_out.txt", "w") as outfile:
        outfile.write("\n".join(map(str, aligned)))

    print("Edit distance =", aligned[0])


if __name__ == "__main__":
    main()
