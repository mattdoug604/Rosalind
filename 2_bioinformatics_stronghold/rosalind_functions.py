#!/usr/bin/python
# rosalind_functions.py

import re

def parseFasta(file_name):
    heads = []
    seqs = {}

    with open(file_name, 'r') as f:
        for num, line in enumerate(f):
            if '>' in line:
                heads.append(num)
    heads.append(sum(1 for line in open(file_name)))

    f = open(file_name, 'r')
    lines = f.readlines()
    for i in range(len(heads)-1):
        h = lines[heads[i]].replace('\n', '')
        l = lines[heads[i]+1:heads[i+1]]
        seqs[h] = ''.join(l).replace('\n', '')

    return(seqs)

def codonTable():
    ''' build a dictionary of codons and corresponding amino acids '''
    bases = ["U", "C", "A", "G"]
    amino_acids = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
    codons = [a+b+c for a in bases for b in bases for c in bases]
    codon_table = dict(zip(codons, amino_acids))

    return(codon_table)
