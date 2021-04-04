#!/usr/bin/env python3

"""
Rosalind: Bioinformatics Stronghold
Problem: Counting Unrooted Binary Trees
URL: http://rosalind.info/problems/cunr/

Given: A positive integer n (n≤1000).
Return: The value of b(n) modulo 1,000,000.
"""

if __name__ == "__main__":
    # A quick function to calculate the double factorial of a given number
    doublefactorial = lambda n: n * doublefactorial(n - 2) if n > 1 else 1

    # Read the number of leaves, n.
    n = int(open("problem_datasets/rosalind_cunr.txt", "r").read())

    # The number of trees on n leaves is the double factorial, (2n-5)!!
    print(doublefactorial(2 * n - 5) % 1000000)
