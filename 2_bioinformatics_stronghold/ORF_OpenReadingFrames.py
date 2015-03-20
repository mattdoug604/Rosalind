#!/usr/bin/python
# Given: A DNA string s of length at most 1 kbp in FASTA format.
# Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

# Start codon = ATG encoding Methionine
# Stop codons = TAA, TAG, or TGA

import re

# create a codon table dictionary
bases = ["T", "C", "A", "G"]
amino_acids = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
codons = [a+b+c for a in bases for b in bases for c in bases]
codon_table = dict(zip(codons, amino_acids))

# function to generate the reverse complement of the sequence (b/c DNA is double stranded!)
def RevComp(seq):
    seq_dict = { 'A':'T', 'T':'A', 'G':'C', 'C':'G' }
    return ''.join([seq_dict[base] for base in reversed(seq)])

def RawTranslate(seq):
    peptides = ['' for x in range(6)]
    rev = RevComp(seq)
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

def FindOrfs(peptides):
    starts = []
    pep_list = []
    for i in range(len(peptides)):
        for j in range(len(peptides[i])):
            if peptides[i][j] == 'M':
                starts.append([i,j])
    for j in starts:
        p = peptides[j[0]]
        p = p[j[1]:len(p)]
        q = re.search('M[A-Z]*\*', p)
        if q != None:
            pep_list.append(q.group())
    return list(set(pep_list))
        
# open file for reading
seq = ''
fasta = open('rosalind_orf.txt', 'r')
for line in fasta:
    if not line.startswith('>'):
        seq += line.strip()

peptides = RawTranslate(seq)
orfs = FindOrfs(peptides)
for o in orfs:
    print o[:-1]
