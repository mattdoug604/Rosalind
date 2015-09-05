#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Ordering Strings of Varying Length Lexicographically 
URL: http://rosalind.info/problems/lexv/

Given: A permutation of at most 12 symbols defining an ordered alphabet A and a
positive integer n (n <= 4).
Return: All strings of length at most n formed from A, ordered lexicographically.
(Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on
the order in which the symbols are given.)
'''

'''
EXAMPLE INPUT:
D N A
3

EXAMPLE OUTPUT:
D DD DDD DDN DDA DN DND DNN DNA DA DAD DAN DAA N ND NDD NDN NDA NN NND NNN NNA
NA NAD NAN NAA A AD ADD ADN ADA AN AND ANN ANA AA AAD AAN AAA
'''

from itertools import product

def generate_strings(alpha, n):
    strings = []
    for i in range(1, n+1):
        strings += [''.join(j) for j in product(alpha, repeat=i)]

    strings = sorted(strings, key=lambda s: [alpha.index(ch) for ch in s])
    
    return strings


def main():
    with open('problem_datasets/rosalind_lexv.txt', 'r') as infile:
        alpha = infile.readline().strip().split(' ')
        n = int(infile.readline())

    strings = generate_strings(alpha, n)
    
    with open('output/rosalind_lexv_out.txt', 'w') as outfile:
        outfile.write('\n'.join(strings))


if __name__ == '__main__':
    main()
