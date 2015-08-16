#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Global Alignment with Constant Gap Penalty
URL: http://rosalind.info/problems/gcon/

Given: Two protein strings s and t in FASTA format (each of length at most 1000 aa).
Return: The maximum alignment score between s and t. Use:
    The BLOSUM62 scoring matrix.
    Constant gap penalty equal to 5.
'''

'''
EXAMPLE INPUT:
>Rosalind_79
PLEASANTLY
>Rosalind_41
MEANLY

EXAMPLE OUTPUT:
13
'''

from rosalind_utils import parse_fasta, print_matrix

def scoring_matrix(path):
    ''' Format a mutli-line text file containing substitution scores
        into a dictonary.
    '''
    with open(path, 'r') as f:
        lines = f.read().strip().split('\n')

    costs = {}
    for i in lines:
        l = i.split(' ')
        costs[' '.join(l[:2])] = l[2]

    return(costs)


def get_score(matrix, a, b):
    ''' Retrieve the score from the scoring matrix. '''
    key = ' '.join((a, b))
    cost = matrix[key]
    return(int(cost))


def alignment_score(s, t, matrix, gap):
    ''' Returns two matrices of the edit distance and edit alignment between
        strings s and t.
    '''

    # Score of best alignment ending with a match or mismatch.
    M = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    # Initialize the gap matrices with an arbitrarily small number.
    # Score of best alignment ending with a space in X.
    X = [[-9999 for j in range(len(t)+1)] for i in range(len(s)+1)]
    # Score of best alignment ending with a space in Y.
    Y = [[-9999 for j in range(len(t)+1)] for i in range(len(s)+1)]

    
    for i in range(1, len(s)+1):
        M[i][0] = gap
    for j in range(1, len(t)+1):
        M[0][j] = gap

    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            X[i][j] = max([M[i-1][j] + gap,
                           X[i-1][j]])
            Y[i][j] = max([M[i][j-1] + gap,
                           Y[i][j-1]])
            M[i][j] = max([M[i-1][j-1] + get_score(matrix, s[i-1], t[j-1]),
                           X[i][j],
                           Y[i][j]])
    
    # The max possible score is found at the bottom-right corner of the matrix
    return(M[-1][-1])


def main():
    s, t = parse_fasta('problem_datasets/rosalind_gcon.txt', True)
    scores = scoring_matrix('data/BLOSUM62.txt')

    max_score = alignment_score(s, t, scores, -5)
    print(max_score)
    

if __name__ == '__main__':
    main()
