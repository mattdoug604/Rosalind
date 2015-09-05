#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Interleaving Two Motifs
URL: http://rosalind.info/problems/scsp/

Given: Two DNA strings s and t.
Return: A shortest common supersequence of s and t. If multiple solutions exist,
you may output any one.
'''

'''
EXAMPLE INPUT:
ATCTGAT
TGCATA

EXAMPLE OUTPUT:
ATGCATGAT
'''

from rosalind_utils import parse_fasta, print_matrix

def shortest_sub(s, t):
    m = len(s)
    n = len(t)

    # Initialize the matrix.
    l = [[[] for x in range(n+1)] for y in range(m+1)]

    # Fill in the matrix.
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                l[i][j] = 0
            elif s[i-1] == t[j-1]:
                l[i][j] = l[i-1][j-1]+1
            else:
                l[i][j] = max(l[i-1][j], l[i][j-1])

    print('The shortest common subsequence should be', m + n - l[-1][-1], 'bases long.')
    print_matrix(l, s, t)

    # Traceback from the bottom corner of the matrix to build the substring.
    i = m
    j = n
    lcs = ''

    while i>0 and j>0:
        if s[i-1] == t[j-1]:
            lcs = s[i-1] + lcs
            i -= 1
            j -= 1
        elif l[i-1][j] > l[i][j-1]:
            i -= 1
        else:
            j -= 1

    print('longest common subsequence =', lcs)
    
    # Fill out the subsequence with the remaining char.
   
    return 
    
        
def main():
    with open('problem_datasets/rosalind_scsp.txt', 'r') as infile:
        s, t = infile.read().strip().split('\n')

    print(shortest_sub(s, t))
        

if __name__ == '__main__':
    main()
