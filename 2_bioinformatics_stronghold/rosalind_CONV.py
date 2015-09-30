#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Comparing Spectra with the Spectral Convolution
URL: http://rosalind.info/problems/conv/

Given: Two multisets of positive real numbers S1 and S2. The size of each 
multiset is at most 200.

Return: The largest multiplicity of S1⊖S2, as well as the absolute value of 
the number x maximizing (S1⊖S2)(x) (you may return any such value if multiple 
solutions exist).
'''

from decimal import Decimal

def largest_multiplicity(s, t):
    # Calculate the Minkowski setserence from both sets.
    sets = {}
    for i in s:
        for j in t:
            d = i - j
            if d in sets:
                sets[d] += 1
            else:
                sets[d] = 1
    
    # Find the largest multiplicity and return it.
    largest = max((v, k) for k ,v in sets.items())
    
    return largest
    
    
def main():
    with open('problem_datasets/rosalind_conv.txt', 'r') as infile:
        s, t = [[Decimal(x) for x in line.split()] for line in infile.read().strip().split('\n')]      
        
    print('\n'.join(map(str, largest_multiplicity(s, t))))
    

if __name__ == '__main__':
    main()