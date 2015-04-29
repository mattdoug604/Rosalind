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

    ''' ok, I feel like this one is kind of cheating since itertools.product()
        returns the strings already in the proper order. I'll try and come
        back and do this 'by hand' at some point (as a learning exercise). '''
    strings = [''.join(i) for i in product(alpha, repeat=n)]
    
    with open('rosalind_lexf_out.txt', 'w') as outfile:
        for s in strings:
            outfile.write(s)
            outfile.write('\n')

if __name__ == '__main__':
    main()
