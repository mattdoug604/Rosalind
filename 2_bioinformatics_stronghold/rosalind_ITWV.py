#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Finding Disjoint Motifs in a Gene
URL: http://rosalind.info/problems/itwv/

Given: A text DNA string s of length at most 10 kbp, followed by a collection of
n (n <= 10) DNA strings of length at most 10 bp acting as patterns.
Return: An n×n matrix M for which Mj,k = 1 if the jth and kth pattern strings
can be interwoven into s and Mj,k = 0 otherwise.
 
EXAMPLE INPUT:
GACCACGGTT
ACAG
GT
CCG

EXAMPLE OUTPUT:
0 0 1
0 1 0
1 0 0
"""
from itertools import combinations_with_replacement as comb_r
from os.path import dirname, join

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_itwv.txt")


def is_superstring(a, b, superstr):
    # Check if two strings can be interwoven into a superstring.
    if len(superstr) == 0:
        return True
    elif a[0] == b[0] == superstr[0]:
        return is_superstring(a[1:], b, superstr[1:]) or is_superstring(a, b[1:], superstr[1:])
    elif a[0] == superstr[0]:
        return is_superstring(a[1:], b, superstr[1:])
    elif b[0] == superstr[0]:
        return is_superstring(a, b[1:], superstr[1:])
    else:
        return False


def find_disjoint_motifs(s, patterns):
    # Initialize the matrix that will hold 1 at position i, j if pattern[i] and
    # pattern[j] can be interwoven into a superstring in s, or 0 if they can't.
    matrix = [[0 for j in range(len(patterns))] for i in range(len(patterns))]

    # For each unique combination of patterns...
    for i in list(comb_r((i for i in range(len(patterns))), 2)):
        a = patterns[i[0]]
        b = patterns[i[1]]

        for j in range(len(s) - len(a) - len(b) + 1):
            superstr = s[j : j + len(a) + len(b)]

            # Add a character outside the alphabet to avoid out of range errors.
            if is_superstring(a + "$", b + "$", superstr):

                # If, for example, patterns 3 and 1 can form a superstring,
                # patterns 1 and 3 can as well.
                matrix[i[0]][i[1]] = 1
                matrix[i[1]][i[0]] = 1
                break

    return matrix


def main():
    # Read in string, s, and a list of patterns.
    with open(INPUT_FILE, "r") as infile:
        s = infile.readline().strip()
        patterns = infile.read().strip().split("\n")

    # Build and fill out the matrix.
    matrix = find_disjoint_motifs(s, patterns)

    # Write answer.
    with open("output/rosalind_itwv_out.txt", "w") as outfile:
        for i in matrix:
            outfile.write(" ".join(map(str, i)) + "\n")

    for i in matrix:
        print(" ".join(map(str, i)))


if __name__ == "__main__":
    main()
