#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Edit Distance
URL: http://rosalind.info/problems/edit/

Given: Two protein strings s and t in FASTA format (each of length at most 1000
aa).
Return: The edit distance dE(s,t).

EXAMPLE INPUT:
>Rosalind_39
PLEASANTLY
>Rosalind_11
MEANLY

...translates to a matrix that holds the distances between all prefixes of the
1st string and all prefixes of the 2nd.

       M E A N L Y
  [ 0  1 2 3 4 5 6]
P [ 1  1 2 3 4 5 6]
L [ 2  2 2 3 4 4 5]
E [ 3  3 2 3 4 5 5]
A [ 4  4 3 2 3 4 5]
S [ 5  5 4 3 3 4 5]
A [ 6  6 5 4 4 4 5]
N [ 7  7 6 5 4 5 5]
T [ 8  8 7 6 5 5 6]
L [ 9  9 8 7 6 5 6]
Y [10 10 9 8 7 6 5]

EXAMPLE OUTPUT:
5
"""

from utils import parse_fasta


def edit_dist(s, t):
    """Takes two DNA strings, of lengths m and n, and returns the edit distance
    between them. This is accomplished by building a matrix, l, that holds
    the distances between all prefixes of the 1st string and all prefixes of
    the 2nd. The final edit distance is then the value at l[m, n].
    """
    m, n = len(s), len(t)

    # Initialize the distance matrix.
    d = [[0 for j in range(n + 1)] for i in range(m + 1)]

    # Each cell in the first row and column recieves a gap penalty (-1).
    for i in range(1, m + 1):
        d[i][0] = i
    for j in range(1, n + 1):
        d[0][j] = j

    # Fill in the distance matrix.
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                d[i][j] = d[i - 1][j - 1]  # a match
            else:
                d[i][j] = min(
                    d[i - 1][j] + 1,  # a deletion
                    d[i][j - 1] + 1,  # an insertion
                    d[i - 1][j - 1] + 1,
                )  # a substitution

    # The edit distance is the last cell of the distance matrix.
    edit_dist = d[m][n]

    return edit_dist


def main():
    s, t = parse_fasta("problem_datasets/rosalind_edit.txt")

    print(edit_dist(s, t))


if __name__ == "__main__":
    main()
