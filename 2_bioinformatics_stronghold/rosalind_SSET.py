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

def subsets(n):
    return(2**n)


def main():
    with open('problem_datasets/rosalind_sset.txt', 'r') as infile:
        n = int(infile.readline().strip())

    answer = subsets(n) % 1000000
    print(answer)


if __name__ == '__main__':
    main()
