#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Finding a Shared Spliced Motif
URL: http://rosalind.info/problems/lcsq/

Given: Two DNA strings s and t (each having length at most 1 kbp) in FASTA format.
Return: A longest common subsequence of s and t. (If more than one solution exists, you may return any one.)
'''

'''
EXAMPLE INPUT:
>Rosalind_23
AACCTTGG
>Rosalind_64
ACACTGTGA

EXAMPLE OUTPUT:
AACTGG
'''

from rosalind_utils import parseFasta

def len_table(s, t, m, n):
    l = [[[] for x in range(n+1)] for y in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                l[i][j] = 0
            elif s[i-1] == t[j-1]:
                l[i][j] = l[i-1][j-1]+1
            else:
                l[i][j] = max(l[i-1][j], l[i][j-1])

    return(l, l[m][n])


def longest_sub(s, t):
    i = len(s)
    j = len(t)
    table, max_l = len_table(s, t, len(s), len(t))
    seq = ''

    while i>0 and j>0:
        if s[i-1] == t[j-1]:
            seq += s[i-1]
            i -= 1
            j -= 1
        elif table[i-1][j] > table[i][j-1]:
            i -= 1
        else:
            j -= 1

    print('The longest common subsequence is', max_l, 'bases long.')
    return(''.join(seq[::-1]))
    
        
def main():
    strings = list(parseFasta('problem_datasets/rosalind_lcsq.txt').values())
    seq = longest_sub(strings[0], strings[1])

    with open('output/rosalind_lcsq_out.txt', 'w') as outfile:
        outfile.write(seq)
        

if __name__ == '__main__':
    main()
