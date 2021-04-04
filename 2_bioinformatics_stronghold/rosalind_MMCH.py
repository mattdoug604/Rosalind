#!/usr/bin/env python3

"""
Rosalind: Bioinformatics Stronghold
Problem: Maximum Matchings and RNA Secondary Structures
URL: http://rosalind.info/problems/mmch/

Given: An RNA string s of length at most 100.
Return: The total possible number of maximum matchings of basepair edges in the
bonding graph of s.
"""

"""
EXAMPLE INPUT:
>Rosalind_92
AUGCUUC

EXAMPLE OUTPUT:
6
"""

from rosalind_utils import parse_fasta


def count_bases(s, a, b):
    a_count, b_count = map(s.count, [a, b])

    return max(a_count, b_count), min(a_count, b_count)


def count_permutations(n, k):
    """Partial permutations is an ordering of only k objects taken from a
    collection of n objects (where k <= n).
    """
    count = 1
    for i in range(n, n - k, -1):
        count *= i

    return count


def max_matches(s):
    """The maximum possible matchings is the greatest number of edges that can
    be formed by joining inequal numbers of A's and U's/C's and G's.
    """
    n1, k1 = count_bases(s, "A", "U")
    n2, k2 = count_bases(s, "C", "G")
    matches = count_permutations(n1, k1) * count_permutations(n2, k2)

    return matches


def main():
    s = parse_fasta("problem_datasets/rosalind_mmch.txt")

    print(max_matches(s))


if __name__ == "__main__":
    main()
