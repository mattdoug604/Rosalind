#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Partial Permutations
URL: http://rosalind.info/problems/pper/

Given: Positive integers n and k such that 100>=n>0 and 10>=k>0.
Return: The total number of partial permutations P(n,k), modulo 1,000,000.
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
