#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Calculating Expected Offspring
URL: http://rosalind.info/problems/iev/

Given: Six positive integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

1. AA-AA
2. AA-Aa
3. AA-aa
4. Aa-Aa
5. Aa-aa
6. aa-aa

Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.
'''

def main():
    with open('problem_datasets/rosalind_iev.txt', 'r') as infile:
        s = [float(i) for i in infile.read().split()]

    expected = (s[0]*1 + s[1]*1 + s[2]*1 + s[3]*3/4 + s[4]*1/2 + s[5]*0)*2
    print '%.1f' % expected
    
if __name__ == '__main__':
    main()
