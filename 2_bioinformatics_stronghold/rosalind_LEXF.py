#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Enumerating k-mers Lexicographically
URL: http://rosalind.info/problems/lexf/

Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n <= 10).
Return: All strings of length n that can be formed from the alphabet, ordered lexicographically.
'''

from itertools import product


def main():
    with open('problem_datasets/rosalind_lexf.txt', 'r') as infile:
        alpha = infile.readline().strip().split(' ')
        n = int(infile.readline())

    ''' ok, this one is kind of cheating since itertools.product() returns the
        strings already in lexographical order.
    '''
    strings = [''.join(i) for i in product(alpha, repeat=n)]
    
    with open('output/rosalind_lexf_out.txt', 'w') as outfile:
        for s in strings:
            outfile.write(s + '\n')


if __name__ == '__main__':
    main()
