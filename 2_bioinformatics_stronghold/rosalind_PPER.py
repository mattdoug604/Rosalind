#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Partial Permutations
URL: http://rosalind.info/problems/pper/

Given: Positive integers n and k such that 100 >= n > 0 and 10 >= k > 0.
Return: The total number of partial permutations P(n,k), modulo 1,000,000.
"""
from os.path import dirname, join

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_pper.txt")

if __name__ == "__main__":
    with open(INPUT_FILE, "r") as f:
        n, k = map(int, f.read().strip().split(" "))

    count = 1
    for i in range(n, n - k, -1):
        count *= i

    print(count % 1000000)
