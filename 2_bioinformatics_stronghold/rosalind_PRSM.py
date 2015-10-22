#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Matching a Spectrum to a Protein
URL: http://rosalind.info/problems/prsm/

Given: A positive integer n followed by a collection of n protein strings s1, 
s2, ..., sn and a multiset R of positive numbers (corresponding to the complete spectrum of some unknown protein string).

Return: The maximum multiplicity of R⊖S[sk] taken over all strings sk, 
followed by the string sk for which this maximum multiplicity occurs (you may 
output any such value if multiple solutions exist).
'''

from rosalind_utils import mass_to_aa


def main():
    with open('problem_datasets/rosalind_prsm.txt', 'r') as infile:
        n = int(infile.readline().strip())
        s = [infile.readline().strip() for i in range(n)]
        r = [float(i) for i in infile.read().strip().split('\n')]
    
    for i in r:
        print(mass_to_aa(i))


if __name__ == '__main__':
    main()