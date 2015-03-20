#!/usr/bin/python
# PERM_EnumeratingGeneOrders.py

'''
Given: A positive integer n<=7.
Return: The total number of permutations of length n, followed by a list of
    all such permutations (in any order).
'''

import itertools

with open('rosalind_perm.txt', 'r') as infile:
    n = int(infile.read().strip())

ints = [str(x) for x in range(1, n+1)]
perms = list(itertools.permutations(ints))

with open('rosalind_perm_out.txt', 'w') as outfile:
    outfile.write(str(len(perms))+'\n')
    for i in perms:
        outfile.write(' '.join(i)+'\n')
