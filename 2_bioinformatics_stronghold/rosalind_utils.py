#!/usr/bin/python

''' This file contains a collection of functions that I've been using repeatedly
    in the Rosalind problems.
'''

def codon_table(base_type='T'):
    ''' Builds a dictionary of codons and corresponding amino acids '''
    bases = ['T', 'C', 'A', 'G']
    if base_type == 'U':
        bases[0] = 'U'
    
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    codons = [a+b+c for a in bases for b in bases for c in bases]
    codon_table = dict(zip(codons, amino_acids))

    return(codon_table)


def parse_fasta(path):
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


def rev_comp(seq):
    if 'U' in seq:
        seq_dict = { 'A':'U', 'U':'A', 'G':'C', 'C':'G' }
    else:
        seq_dict = { 'A':'T', 'T':'A', 'G':'C', 'C':'G' }

    return(''.join([seq_dict[base] for base in reversed(seq)]))
