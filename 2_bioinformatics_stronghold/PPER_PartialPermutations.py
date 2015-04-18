#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Calculating Protein Mass
URL: http://rosalind.info/problems/prtm/

Given: A protein string P of length at most 1000 aa.
Return: The total weight of P. Consult the monoisotopic mass table.
'''

def countPermutations(n, k):
    count = 1
    for i in range(n, n-k, -1):
        count *= i

    print(count % 1000000)

if __name__ == '__main__':
    n = 90
    k = 8
    countPermutations(n, k)
