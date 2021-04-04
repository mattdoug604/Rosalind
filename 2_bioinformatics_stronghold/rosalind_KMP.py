#!/usr/bin/env python3

'''
Rosalind: Bioinformatics Stronghold
Problem: Speeding Up Motif Finding 
URL: http://rosalind.info/problems/kmp/

Given: A DNA string s (of length at most 100 kbp) in FASTA format.
Return: The failure array of s.
'''

'''
EXAMPLE INPUT:
>Rosalind_87
CAGCATGGTATCACAGCAGAG

EXAMPLE OUTPUT:
0 0 0 1 2 0 0 0 0 0 0 1 2 1 2 3 4 5 3 0 0
'''

from rosalind_utils import parse_fasta

def failure_array(s):
    f = [0 for i in range(len(s))]
    n = len(s)
    k = 1 # position in the string
    j = 0 # length of the longest substring

    while k < n:
        if s[k] == s[j]:
            j += 1
            f[k] = j
            k += 1
        else:
            if j != 0:
                j = f[j-1]
            else:
                f[k] = 0
                k += 1

    return f


def main():
    s = parse_fasta('problem_datasets/rosalind_kmp.txt')
    
    with open('output/rosalind_kmp_out.txt', 'w') as outfile:
        outfile.write(' '.join(map(str, failure_array(s))))


if __name__ == '__main__':
    main()
