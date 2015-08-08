#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Global Alignment with Scoring Matrix
URL: http://rosalind.info/problems/glob/

Given: Two protein strings s and t in FASTA format (each of length at most 1000 aa).
Return: The maximum alignment score between s and t. Use:
    The BLOSUM62 scoring matrix.
    Linear gap penalty equal to 5 (i.e., a cost of -5 is assessed for each gap symbol).
'''

'''
EXAMPLE INPUT:
>Rosalind_67
PLEASANTLY
>Rosalind_17
MEANLY

EXAMPLE OUTPUT:
8
'''

from rosalind_utils import parse_fasta

def build_matrix(path):
    ''' Format a mutli-line string of the scoring matrix into a usable format. '''
    with open(path, 'r') as f:
        lines = f.read().strip().split('\n')

    costs = {}
    for i in lines:
        l = i.split(' ')
        costs[' '.join(l[:2])] = l[2]

    return(costs)


def get_score(matrix, a, b, gap=-5):
    ''' Return the score from the scoring matrix. '''
    if a == '-' or b == '-':
        return(gap)
    else:
        key = ' '.join((a, b))
        cost = matrix[key]

    return(int(cost))


def print_matrix(matrix, s, t):
    ''' Optional: Print out the given matrix. '''
    print('Writing matrix...\n')
    print('      ' + '   '.join(t))
    for x, m in enumerate(matrix):
        if x > 0:
            line = s[x-1] +' [' + ' '.join(map(str, m)) + ']'
        else:
            line = '  [' + ' '.join(map(str, m)) + ']'
        print(line)
    print()


def alignment_score(s, t, matrix, gap):
    ''' Returns two matrices of the edit distance and edit alignment between
        strings s and t.
    '''

    # Initialize the matrices with zeros.
    d = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    
    for i in range(1, len(s)+1):
        d[i][0] = i * gap
    for j in range(1, len(t)+1):
        d[0][j] = j * gap

    # Fill in the Distance and Backtrack matrices.
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            cost = [ d[i-1][j-1] + get_score(matrix, s[i-1], t[j-1]),
                     d[i-1][j] + gap,
                     d[i][j-1] + gap ]
            d[i][j] = max(cost)

    #print_matrix(d, s, t)

    # The max possible score is found at the bottom-right corner of the matrix
    return(d[-1][-1])

   
def main():
    s, t = parse_fasta('problem_datasets/rosalind_glob.txt', True)
    score_matrix = build_matrix('BLOSUM62.txt')

    max_score = alignment_score(s, t, score_matrix, -5)
    print(max_score)
        

if __name__ == '__main__':
    main()
