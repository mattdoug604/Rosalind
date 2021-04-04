#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Counting Rooted Binary Trees
URL: http://rosalind.info/problems/root/

Given: A positive integer n (n≤1000).
Return: The value of B(n) modulo 1,000,000.
"""
from os.path import dirname, join

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_root.txt")


if __name__ == "__main__":
    # A quick function to calculate the double factorial of a given number
    doublefactorial = lambda n: n * doublefactorial(n - 2) if n > 1 else 1

    # Read the number of leaves, n.
    n = int(open(INPUT_FILE, "r").read())

    # The number of trees on n leaves is the double factorial, (2n-3)!!
    print(doublefactorial(2 * n - 3) % 1000000)
