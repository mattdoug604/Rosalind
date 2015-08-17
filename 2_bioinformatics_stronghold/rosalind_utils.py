#!/usr/bin/python

''' This file contains a collection of functions that I've been using repeatedly
    in the Rosalind problems.
'''

def aa_mass():
    ''' Returns a dictonary of monoisotopic amino acid masses. '''
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


def codon_table(base_type='T'):
    ''' Return a dictionary of codons and corresponding amino acids '''
    bases = ['T', 'C', 'A', 'G']
    if base_type == 'U':
        bases[0] = 'U'
    
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    codons = [a+b+c for a in bases for b in bases for c in bases]
    codon_table = dict(zip(codons, amino_acids))

    return(codon_table)


def parse_fasta(path, no_id=False):
    ''' Read in a Fasta file. If no_id is set to false, return a dictonary of
        sequences with associated headers; else return a list of sequences only.
    '''
    ids = []
    seqs = []
    
    with open(path, 'r') as f:
        for line in f.readlines():
            if line.startswith('>'):
                ids.append(line[1:].strip())
                seqs.append('')
            else:
                seqs[-1] += line.strip()

    if no_id == False:
        return(dict(zip(ids, seqs)))
    else:
        return(seqs)


def print_matrix(matrix, y, x):
    ''' Print out the given 2D matrix with axis labels. Matrix rows must be the
        same length.
    '''
    # Determine the spacing between columns.
    spacing = [0 for i in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        max_l = 0
        for j in range(len(matrix)):
            l = len(str(matrix[j][i]))
            if l > max_l:
                max_l = l
                spacing[i] = max_l

    # Print the x-axis.
    x = ' ' + x
    spacing = [len(max(y, key=len))] + spacing
    x_axis = ' '*spacing[0]
    for i, ch in enumerate(x):
        x_axis += ' '*spacing[i+1] + ch
    print(x_axis)

    # Print each row of the matrix with y-label.
    y = ' ' + y
    for i in range(len(matrix)):
        line = y[i]
        for j in range(len(matrix[i])):
            line += ' '*(spacing[j+1]-len(str(matrix[i][j]))+1) + str(matrix[i][j])
        print(line)

    
def rev_comp(seq):
    ''' Return the reverse complement of a given DNA or RNA string. '''
    if 'U' in seq:
        seq_dict = { 'A':'U', 'U':'A', 'G':'C', 'C':'G' }
    else:
        seq_dict = { 'A':'T', 'T':'A', 'G':'C', 'C':'G' }

    return(''.join([seq_dict[base] for base in reversed(seq)]))


def scoring_matrix(path):
    ''' Read a text file of a scoring matrix and return a list of scores. The
        first element in the list is the amino acids.
    '''
    with open(path, 'r') as f:
        lines = f.read().strip().split('\n')

    scores = [lines[0].split()] + [l[1:].split() for l in lines[1:]]
    return(scores)
