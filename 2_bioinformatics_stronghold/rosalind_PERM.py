#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Enumerating Gene Orders
URL: http://rosalind.info/problems/perm/

Given: A positive integer n <= 7.
Return: The total number of permutations of length n, followed by a list of all
such permutations (in any order).
"""

from itertools import permutations


def main():
    with open("problem_datasets/rosalind_perm.txt", "r") as infile:
        n = int(infile.read())

    ints = [str(x) for x in range(1, n + 1)]
    perms = list(permutations(ints))

    with open("output/rosalind_perm_out.txt", "w") as outfile:
        outfile.write(str(len(perms)) + "\n")
        for i in perms:
            outfile.write(" ".join(i) + "\n")


if __name__ == "__main__":
    main()
