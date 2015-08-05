#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Open Reading Frames
URL: http://rosalind.info/problems/orf/

Given: A DNA string s of length at most 1 kbp in FASTA format.
Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.
'''

import rosalind_utils
import re


def raw_translate(seq):
    ''' Translate all 6 ORFs (3 for the forward strand, 3 for the reverse). '''
    table = rosalind_utils.codon_table()
    peptides = ['' for x in range(6)]
    rev = rosalind_utils.rev_comp(seq)
    
    for i in range(3):
        for j in range(i, len(seq), 3):
            codon = seq[j:j+3]
            aa = table.get(codon,'-')
            peptides[i] += aa
        for j in range(i, len(rev), 3):
            codon = rev[j:j+3]
            aa = table.get(codon,'-')
            peptides[i+3] += aa

    return(peptides)


def find_orfs(peptides):
    starts = []
    pep_list = []

    ''' Identify the position of each Methionine (corresponding to a start
        codon) in each ORF.
    '''
    for i in range(len(peptides)):
        for j in range(len(peptides[i])):
            if peptides[i][j] == 'M':
                starts.append([i,j])

    ''' From each identified start position, search for an interval from an 'M'
        to a stop codon ('*') corresponding to a possible peptide.
    '''             
    for j in starts:
        p = peptides[j[0]]
        p = p[j[1]:len(p)]
        q = re.search('M[A-Z]*\*', p)
        if q != None:
            pep_list.append(q.group())
    
    return(list(set(pep_list)))  # use set() to eliminate any duplicates


def main():
    with open('problem_datasets/rosalind_orf.txt', 'r') as infile:
        seq = ''
        for line in infile:
            if not line.startswith('>'):
                seq += line.strip()

    peptides = raw_translate(seq)
    orfs = find_orfs(peptides)

    with open('output/rosalind_orf_out.txt', 'w') as outfile:
        for o in orfs:
            outfile.write(o[:-1] + '\n')


if __name__ == '__main__':
    main()
