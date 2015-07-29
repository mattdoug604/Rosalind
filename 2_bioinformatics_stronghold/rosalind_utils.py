#!/usr/bin/python

''' This file contains a bunch of functions that I've been using in many of the
    Rosalind problems.
'''

def parseFasta(path):
    ''' Reads a text file containing one or more FASTA sequences and returns a
        dictionary of ids and corresponding sequences.
    '''
    fastas = {}
    
    with open(path, 'r') as f:
        for line in f.readlines():
            if line.startswith('>'):
                head = line[1:].strip()
                fastas[head] = ''
            else:
                fastas[head] += line.strip()

    return(fastas)


def codonTable(seq_type='dna'):
    ''' Builds a dictionary of codons and corresponding amino acids '''
    bases = ["T", "C", "A", "G"]
    if seq_type == 'rna':
        bases[0] = 'U'
    
    amino_acids = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
    codons = [a+b+c for a in bases for b in bases for c in bases]
    codon_table = dict(zip(codons, amino_acids))

    return(codon_table)
