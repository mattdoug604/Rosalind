#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Counting Subsets
URL: http://rosalind.info/problems/sset/

Given: A positive integer n (n <= 1000).
Return: The total number of subsets of {1,2,…,n} modulo 1,000,000.
 
EXAMPLE INPUT:
3

EXAMPLE OUTPUT:
8
"""
from os.path import dirname, join

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_sset.txt")


if __name__ == "__main__":
    with open(INPUT_FILE, "r") as infile:
        n = int(infile.read())

    print(2 ** n % 1000000)
