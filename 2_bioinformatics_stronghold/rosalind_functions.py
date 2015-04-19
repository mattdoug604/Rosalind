#!/usr/bin/python

''' This file contains a bunch of functions that I've been using in many of the
    Rosalind problems.
'''
import re

def parseFasta(path):
    ''' Reads a text file containing one or more FASTA sequences and seperates
        them into a dictionary of sequence headers and corresponding sequences.
    '''
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

def codonTable(seq_type='dna'):
    ''' Builds a dictionary of codons and corresponding amino acids '''
    bases = ["T", "C", "A", "G"]
    if seq_type == 'rna':
        bases[0] = 'U'
    
    amino_acids = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
    codons = [a+b+c for a in bases for b in bases for c in bases]
    codon_table = dict(zip(codons, amino_acids))

    return(codon_table)
