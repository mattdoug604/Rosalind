#!/usr/bin/env python3

"""
Rosalind: Bioinformatics Stronghold
Problem: Counting Subsets
URL: http://rosalind.info/problems/sset/

Given: A positive integer n (n <= 1000).
Return: The total number of subsets of {1,2,…,n} modulo 1,000,000.
"""

"""
EXAMPLE INPUT:
3

EXAMPLE OUTPUT:
8
"""

if __name__ == "__main__":
    with open("problem_datasets/rosalind_sset.txt", "r") as infile:
        n = int(infile.read())

    print(2 ** n % 1000000)
