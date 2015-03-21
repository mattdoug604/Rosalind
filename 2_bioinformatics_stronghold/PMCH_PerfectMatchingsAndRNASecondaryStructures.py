#!/usr/bin/python
# PMCH_PerfectMatchingsAndRNASecondaryStructures.py

'''
Given: An RNA string s of length at most 80 bp having the same number of
    occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.
Return: The total possible number of perfect matchings of basepair edges in
    the bonding graph of s.
'''

from math import factorial

with open('problem_datasets/rosalind_pmch.txt', 'r') as infile:
    text = infile.read().strip().split('\n')
    rna = ''.join(text[1:])

perfect = factorial(rna.count('A')) * factorial(rna.count('C'))
print(perfect)
