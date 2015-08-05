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


def aa_mass():
    mass_table = { 'A':71.03711,
                   'C':103.00919,
                   'D':115.02694,
                   'E':129.04259,
                   'F':147.06841,
                   'G':57.02146,
                   'H':137.05891,
                   'I':113.08406,
                   'K':128.09496,
                   'L':113.08406,
                   'M':131.04049,
                   'N':114.04293,
                   'P':97.05276,
                   'Q':128.05858,
                   'R':156.10111,
                   'S':87.03203,
                   'T':101.04768,
                   'V':99.06841,
                   'W':186.07931,
                   'Y':163.06333 }

    return(mass_table)

    
def rev_comp(seq):
    if 'U' in seq:
        seq_dict = { 'A':'U', 'U':'A', 'G':'C', 'C':'G' }
    else:
        seq_dict = { 'A':'T', 'T':'A', 'G':'C', 'C':'G' }

    return(''.join([seq_dict[base] for base in reversed(seq)]))
