#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Counting Phylogenetic Ancestors
URL: http://rosalind.info/problems/inod/

Given: A positive integer n (3 <= n <= 10000).
Return: The number of internal nodes of any unrooted binary tree having n leaves.
"""
from os.path import dirname, join

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_inod.txt")

# Rooted vs Unrooted:
# - A rooted binary tree with n leaves has 2n-2 edges, and n-1 internal nodes.
# - An unrooted binary tree with n leaves has 2n-3 edges and n-2 internal nodes
# (picture the root of a tree and it's two edges combining into a single edge).

if __name__ == "__main__":
    with open(INPUT_FILE, "r") as f:
        n = int(f.read())

    print(n - 2)
