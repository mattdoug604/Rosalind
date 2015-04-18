#!/usr/bin/python
# rosalind_functions.py

import re

def parseFasta(path):
    headers = []
    seqs = {}

    with open(path, 'r') as f:
        for num, line in enumerate(f):
            if '>' in line:
                headers.append(num)
    headers.append(sum(1 for line in open(path)))

    with open(path, 'r') as f:
        lines = f.readlines()
        for i in range(len(headers)-1):
            h = lines[headers[i]][1:].replace('\n', '')
            l = lines[headers[i]+1:headers[i+1]]
            seqs[h] = ''.join(l).replace('\n', '')

    return(seqs)

def codonTable():
    ''' build a dictionary of codons and corresponding amino acids '''
    bases = ["T", "C", "A", "G"]
    amino_acids = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
    codons = [a+b+c for a in bases for b in bases for c in bases]
    codon_table = dict(zip(codons, amino_acids))

    return(codon_table)
