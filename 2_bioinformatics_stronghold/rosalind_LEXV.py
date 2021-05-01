#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Ordering Strings of Varying Length Lexicographically 
URL: http://rosalind.info/problems/lexv/

Given: A permutation of at most 12 symbols defining an ordered alphabet A and a
positive integer n (n <= 4).
Return: All strings of length at most n formed from A, ordered lexicographically.
(Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on
the order in which the symbols are given.)
 
EXAMPLE INPUT:
D N A
3

EXAMPLE OUTPUT:
D DD DDD DDN DDA DN DND DNN DNA DA DAD DAN DAA N ND NDD NDN NDA NN NND NNN NNA
NA NAD NAN NAA A AD ADD ADN ADA AN AND ANN ANA AA AAD AAN AAA
"""
from itertools import product
from os.path import dirname, join

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_lexv.txt")


def generate_strings(alpha, n):
    strings = []
    for i in range(1, n + 1):
        strings += ["".join(j) for j in product(alpha, repeat=i)]

    strings = sorted(strings, key=lambda s: [alpha.index(ch) for ch in s])

    return strings


def main():
    with open(INPUT_FILE, "r") as infile:
        alpha = infile.readline().strip().split(" ")
        n = int(infile.readline())

    strings = generate_strings(alpha, n)
    print(*strings, sep="\n")


if __name__ == "__main__":
    main()
