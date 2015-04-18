#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Independent Alleles
URL: http://rosalind.info/problems/lia/

Given: Two positive integers k (k <= 7) and N (N <= 2^k). In this problem, we
    begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two
    children in the 1st generation, each of whom has two children, and so on.
    Each organism always mates with an organism having genotype Aa Bb.
Return: The probability that at least N Aa Bb organisms will belong to the
    k-th generation of Tom's family tree (don't count the Aa Bb mates at each
    level). Assume that Mendel's second law holds for the factors.
'''

def generations(k, n):
    '''
    P(AaBb)
    '''

def main():
    k = 2
    n = 1

    prob = generations(k, n)
    print(prob)

if __name__ == '__main__':
    main()
