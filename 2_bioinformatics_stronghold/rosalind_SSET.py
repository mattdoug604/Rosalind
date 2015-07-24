#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Counting Subsets
URL: http://rosalind.info/problems/sset/

Given: A positive integer n (n <= 1000).
Return: The total number of subsets of {1,2,…,n} modulo 1,000,000.
'''

'''
EXAMPLE INPUT:
3

EXAMPLE OUTPUT:
8
'''

from math import factorial

def binomial(n):
    f = factorial
    return(sum(f(n) // (f(k) * f(n-k)) for k in range(n+1)))


def main():
    with open('problem_datasets/rosalind_sset.txt', 'r') as infile:
        n = int(infile.readline().strip())

    answer = int(binomial(n)) % 1000000
    print(answer)


if __name__ == '__main__':
    main()
