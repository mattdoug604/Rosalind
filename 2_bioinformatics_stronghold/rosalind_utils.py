#!/usr/bin/python

''' This file contains a collection of functions that I've been using repeatedly
    in the Rosalind problems.
'''

#####################################
### ---------- FILE I/O --------- ###
#####################################

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


#####################################
### ----------- TABLES ---------- ###
#####################################
    
def aa_mass(aa):
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

    return(mass_table[aa])


def codon_table(seq_type='rna'):
    ''' Return a dictionary of codons and corresponding amino acids '''
    bases = ['U', 'C', 'A', 'G'] if seq_type == 'rna' else ['T', 'C', 'A', 'G']
    
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    codons = [a+b+c for a in bases for b in bases for c in bases]
    codon_table = dict(zip(codons, amino_acids))

    return(codon_table)


#####################################
### --- SEQUENCE MANIPULATION --- ###
#####################################

def reverse_complement(seq):
    ''' Return the reverse complement of a given DNA or RNA string. '''
    if 'U' in seq:
        seq_dict = { 'A':'U', 'U':'A', 'G':'C', 'C':'G' }
    else:
        seq_dict = { 'A':'T', 'T':'A', 'G':'C', 'C':'G' }

    return(''.join([seq_dict[base] for base in reversed(seq)]))


#####################################
### ----- SEQUENCE ALIGNMENT ---- ###
#####################################

def BLOSUM62():
    return(scoring_matrix('data/blosum62.txt'))


def PAM250():
    return(scoring_matrix('data/pam250.txt'))

    
def scoring_matrix(path):
    ''' Read a text file of a scoring matrix and return a list of scores. The
        first element in the list is the amino acids.
    '''
    with open(path, 'r') as f:
        lines = f.read().strip().split('\n')

    scores = [lines[0].split()] + [l[1:].split() for l in lines[1:]]

    return(scores)


def match_score(scoring_matrix, a, b):
    ''' Return the score from the scoring matrix. '''
    x = scoring_matrix[0].index(a)
    y = scoring_matrix[0].index(b)
    cost = int(scoring_matrix[x+1][y])

    return(cost)


def print_matrix(matrix, y=None, x=None):
    ''' Print out the given 2D matrix with axis labels. Matrix rows must be the
        same length.
    '''
    # If axis labels aren't specified...
    #if len(y) < len(matrix)-1:
    #    y = y + ' '*(len(matrix)-len(y)-1)
    
    # Determine the spacing between columns.
    spacing = [0 for i in range(len(matrix[0])+1)]
    for i in range(len(matrix[0])):
        max_l = 0
        for j in range(len(matrix)):
            l = len(str(matrix[j][i]))
            if l > max_l:
                max_l = l
                spacing[i+1] = max_l

    # Print the x-axis.
    if x is not None:
        x = ' ' + x
        spacing[0] = len(max(y, key=len))
        x_axis = ' '*spacing[0]
        for i, ch in enumerate(x):
            x_axis += ' '*spacing[i+1] + ch
        print(x_axis)

    # Print each row of the matrix with y-label.
    if y is not None:
        y = ' ' + y
        
    for i in range(len(matrix)):
        if y is not None:
            line = y[i]
            for j in range(len(matrix[i])):
                line += ' '*(spacing[j+1]-len(str(matrix[i][j]))+1) + str(matrix[i][j])
        else:
            line = ''
            for j in range(len(matrix[i])):
                line += ' '*(spacing[j]-len(str(matrix[i][j]))+1) + str(matrix[i][j])

        print(line)
