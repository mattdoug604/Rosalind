#!/usr/bin/env python3

'''
Rosalind: Bioinformatics Stronghold
Problem: Open Reading Frames
URL: http://rosalind.info/problems/orf/

Given: A DNA string s of length at most 1 kbp in FASTA format.
Return: Every distinct candidate protein string that can be translated from ORFs
of s. Strings can be returned in any order.
'''

from rosalind_utils import parse_fasta, codon_table, reverse_complement
import re

def raw_translate(seq):
    ''' Translate all 6 ORFs (3 for the forward strand, 3 for the reverse). '''
    table = codon_table('dna')
    peptides = ['' for x in range(6)]
    rev = reverse_complement(seq)
    
    for i in range(3):
        for j in range(i, len(seq), 3):
            codon = seq[j:j+3]
            peptides[i] += table.get(codon, '-')
        for j in range(i, len(rev), 3):
            codon = rev[j:j+3]
            peptides[i+3] += table.get(codon, '-')
    
    return peptides


def find_orfs(peptides):
    starts = []
    pep_list = []

    # Identify the position of each Methionine (corresponding to a start codon)
    # in each ORF.
    for i in range(len(peptides)):
        for j in range(len(peptides[i])):
            if peptides[i][j] == 'M':
                starts.append([i,j])

    # From each identified start position, search for an interval from an 'M' to
    # a stop codon ('*') corresponding to a possible peptide.            
    for j in starts:
        p = peptides[j[0]]
        p = p[j[1]:len(p)]
        q = re.search('M[A-Z]*\*', p)
        if q != None:
            pep_list.append(q.group().rstrip('*')) # Strip the stop codon
    
    return list(set(pep_list))  # use set() to eliminate any duplicates


def main():
    seq = parse_fasta('problem_datasets/rosalind_orf.txt')
            
    peptides = raw_translate(seq)
    orfs = find_orfs(peptides)

    with open('output/rosalind_orf_out.txt', 'w') as outfile:
        outfile.write('\n'.join(orfs))


if __name__ == '__main__':
    main()
