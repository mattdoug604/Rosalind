''' This file contains a collection of functions that I've been using frequently
    in the Rosalind problems.
'''

#####################################
### ---------- FILE I/O --------- ###
#####################################

def parse_fasta(path, no_id=True):
    ''' Read in a Fasta file. If no_id is set to False, return a dictonary of
        sequences with associated headers; otherwise return a list of sequences
        only.
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

    if no_id == True:
        if len(seqs) > 1:
            return seqs
        else:
            return seqs[0]
    else:
        return dict(zip(ids, seqs))


def print_matrix(matrix, ylab=None, xlab=None):
    ''' Print out the given 2D matrix with axis labels. Matrix rows must be the
        same length.
    '''
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
    if xlab is not None:
        xlab = ' ' + xlab
        spacing[0] = len(max(ylab, key=len))
        x_axis = ' ' * spacing[0]
        for i, ch in enumerate(xlab):
            x_axis += ' ' * spacing[i+1] + ch

        print(x_axis)

    # Print each row of the matrix with y-label.
    if ylab is not None:
        ylab = ' ' + ylab
        
    for i in range(len(matrix)):
        if ylab is not None:
            line = ylab[i]
            for j in range(len(matrix[i])):
                line += ' ' * (spacing[j+1]-len(str(matrix[i][j]))+1) + str(matrix[i][j])
        else:
            line = ''
            for j in range(len(matrix[i])):
                line += ' ' * (spacing[j]-len(str(matrix[i][j]))+1) + str(matrix[i][j])

        print(line)


#####################################
### --------- MASS SPEC --------- ###
#####################################
    
def aa_mass(aa):
    ''' Returns the monoisotopic mass of a given amino acid(s). '''
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
    
    mass = 0
    for i in aa:
        try:
            mass += mass_table[i]
        except KeyError:
            print('Error: Could not find a mass for an amino acid %s.' % i)
            return None

    return mass


def mass_to_aa(val, tolerance=0.0001):
    ''' Returns the amino acid corresponding to a given mass. '''
    aa_table = { 71.03711:'A',
                 103.00919:'C',
                 115.02694:'D',
                 129.04259:'E',
                 147.06841:'F',
                 57.02146:'G',
                 137.05891:'H',
                 113.08406:'I',
                 128.09496:'K',
                 113.08406:'L',
                 131.04049:'M',
                 114.04293:'N',
                 97.05276:'P',
                 128.05858:'Q',
                 156.10111:'R',
                 87.03203:'S',
                 101.04768:'T',
                 99.06841:'V',
                 186.07931:'W',
                 163.06333:'Y' }

    for mass, aa in aa_table.items():
        if abs(val - mass) < tolerance:
            return aa

    print('Note: Could not find an amino acid with monoisotopic mass %.5f.' % val)
    return None


#####################################
### -------- TRANSLATION -------- ###
#####################################

def codon_table(seq_type='rna'):
    ''' Return a dictionary of codons and corresponding amino acids '''
    bases = ['U', 'C', 'A', 'G'] if seq_type == 'rna' else ['T', 'C', 'A', 'G']
    
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    codons = [a+b+c for a in bases for b in bases for c in bases]
    codon_table = dict(zip(codons, amino_acids))

    return codon_table


#####################################
### --- SEQUENCE MANIPULATION --- ###
#####################################

def reverse_complement(seq):
    ''' Return the reverse complement of a given DNA or RNA string. '''
    if 'U' in seq:
        seq_dict = { 'A':'U', 'U':'A', 'G':'C', 'C':'G' }
    else:
        seq_dict = { 'A':'T', 'T':'A', 'G':'C', 'C':'G' }

    return ''.join([seq_dict[base] for base in reversed(seq)])


#####################################
### ----- SEQUENCE ALIGNMENT ---- ###
#####################################

def BLOSUM62():
    return scoring_matrix('data/blosum62.txt')


def PAM250():
    return scoring_matrix('data/pam250.txt')

    
def scoring_matrix(path):
    ''' Read a text file of a scoring matrix and return a list of scores. The
        first element in the list is the amino acids.
    '''
    with open(path, 'r') as f:
        lines = f.read().strip().split('\n')

    scores = [lines[0].split()] + [l[1:].split() for l in lines[1:]]

    return scores


def match_score(scoring_matrix, a, b):
    ''' Return the score from the scoring matrix. '''
    x = scoring_matrix[0].index(a)
    y = scoring_matrix[0].index(b)
    cost = int(scoring_matrix[x+1][y])

    return cost
