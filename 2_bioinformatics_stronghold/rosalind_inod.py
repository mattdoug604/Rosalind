#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Counting Phylogenetic Ancestors
URL: http://rosalind.info/problems/inod/

Given: A positive integer n (3 <= n <= 10000).
Return: The number of internal nodes of any unrooted binary tree having n leaves.
'''

'''
Rooted vs Unrooted:
- A rooted binary tree with n leaves has 2n-2 edges, and n-1 internal nodes.
- An unrooted binary tree with n leaves has 2n-3 edges and n-2 internal nodes
(picture the root of a tree and it's two edges combining into a single edge).
'''

def main(n):
    print(n-2)

if __name__ == '__main__':
    n = 6584
    main(n)
