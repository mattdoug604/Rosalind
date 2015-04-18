#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Open Reading Frames
URL: http://rosalind.info/problems/orf/

Given: A DNA string s of length at most 1 kbp in FASTA format.
Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.
'''

from rosalind_functions import codonTable
import re

def revComp(seq):
    '''
    Because DNA is double stranded, we need to generate
    the reverese complement.
    '''
    seq_dict = { 'A':'T', 'T':'A', 'G':'C', 'C':'G' }
    return ''.join([seq_dict[base] for base in reversed(seq)])

def rawTranslate(seq):
    ''' Generate a codon table. '''
    codon_table = codonTable()

    ''' Translate all 6 ORFs (3 for the forward strand,
        3 for the reverse).
    '''
    peptides = ['' for x in range(6)]
    rev = revComp(seq)
    for i in range(3):
        for j in range(i, len(seq), 3):
            codon = seq[j:j+3]
            aa = codon_table.get(codon,'-')
            peptides[i] += aa
        for j in range(i, len(rev), 3):
            codon = rev[j:j+3]
            aa = codon_table.get(codon,'-')
            peptides[i+3] += aa

    return peptides

def findOrfs(peptides):
    starts = []
    pep_list = []

    ''' Identify the position of each Methionine
        (corresponding to a start codon) in each ORF.
    '''
    for i in range(len(peptides)):
        for j in range(len(peptides[i])):
            if peptides[i][j] == 'M':
                starts.append([i,j])

    ''' From each identified start position, search
        for an interval from an 'M' to a stop codon
        ('*') corresponding to a possible peptide.
    '''             
    for j in starts:
        p = peptides[j[0]]
        p = p[j[1]:len(p)]
        q = re.search('M[A-Z]*\*', p)
        if q != None:
            pep_list.append(q.group())

    # use set() to eliminate any duplicates
    return list(set(pep_list))

def main():
    seq = ''

    with open('problem_datasets/rosalind_orf.txt', 'r') as infile:
        for line in infile:
            if not line.startswith('>'):
                seq += line.strip()

    peptides = rawTranslate(seq)
    orfs = findOrfs(peptides)
    for o in orfs:
        print o[:-1]

if __name__ == '__main__':
    main()
