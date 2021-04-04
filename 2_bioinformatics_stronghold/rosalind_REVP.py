#!/usr/bin/env python3

'''
Rosalind: Bioinformatics Stronghold
Problem: Locating Restriction Sites
URL: http://rosalind.info/problems/revp/

Given: A DNA string of length at most 1 kbp in FASTA format.
Return: The position and length of every reverse palindrome in the string having
length between 4 and 12. You may return these pairs in any order.
'''

from rosalind_utils import reverse_complement as rev_comp

def locate_sites(f_dna):
    r_dna = rev_comp(f_dna)

    for i in range(4, 13, 2):
        for j in range(len(f_dna)):
            f = f_dna[j:j+i]
            r = r_dna[len(r_dna)-j-i:len(r_dna)-j]
            if f == r:
                yield j+1, i


def main():
    with open('problem_datasets/rosalind_revp.txt', 'r') as infile:
        dna = ''.join(infile.readlines()[1:]).replace('\n', '')

    with open('output/rosalind_revp_out.txt', 'w') as outfile:
        for site in locate_sites(dna):
            outfile.write(' '.join(map(str, site)) + '\n')

    
if __name__ == '__main__':
    main()
