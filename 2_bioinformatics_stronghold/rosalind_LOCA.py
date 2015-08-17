#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Local Alignment with Scoring Matrix
URL: http://rosalind.info/problems/loca/

Given: Two protein strings s and t in FASTA format (each having length at most 1000 aa).
Return: A maximum alignment score along with substrings r and u of s and t, respectively, which produce this maximum alignment score (multiple solutions may exist, in which case you may output any one). Use:
    The PAM250 scoring matrix.
    Linear gap penalty equal to 5.
'''

'''
EXAMPLE INPUT:
>Rosalind_80
MEANLYPRTEINSTRING
>Rosalind_21
PLEASANTLYEINSTEIN

EXAMPLE OUTPUT:
23
LYPRTEINSTRIN
LYEINSTEIN
'''

from rosalind_utils import parse_fasta, scoring_matrix, print_matrix

def get_score(scores, a, b, gap):
    ''' Return the score from the scoring matrix. '''
    if a == '-' or b == '-':
        return(gap)
    else:
        x = scores[0].index(a)
        y = scores[0].index(b)
        cost = int(scores[x+1][y])

    return(cost)


def substrings(s, t):
    return()

    
def alignment_score(s, t, matrix, gap):
    ''' Returns two matrices of the edit distance and edit alignment between
        strings s and t.
    '''

    # Initialize the matrices with zeros.
    d = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    backtrack = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    
    for i in range(1, len(s)+1):
        d[i][0] = i * gap
    for j in range(1, len(t)+1):
        d[0][j] = j * gap

    # Initialize the maximum alignment score as an arbitarily small value.
    max_score = -9999
    r, u = ('', '')
    best_b = backtrack
    best_d = d

    # Fill in the Similarity and Backtrack matrices.
    for sub in substrings(s, t):
        b = backtrack
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                cost = [ 0,
                         d[i-1][j-1] + get_score(matrix, sub[0][i-1], sub[1][j-1], gap),
                         d[i-1][j] + gap,
                         d[i][j-1] + gap ]
                d[i][j] = max(cost)
                b[i][j] = cost.index(d[i][j])

        # The max possible score is found at the bottom-right corner of the matrix
        score = d[-1][-1]
        if score > max_score:
            max_score = score
            r = sub[0]
            u = sub[1]
            best_b = b
            best_d = d

    #print_matrix(best_d, r, u)
    
    # Initialize the aligned strings as the input strings.
    r_align, u_align = r, u

    # Initialize the values of i,j
    i, j = len(r), len(u)

    # Backtrack to the edge of the matrix starting at the bottom right.
    while i>0 and j>0:
        if backtrack[i][j] == 1: # an insertion
            i -= 1
            u_align = u_align[:j] + '-' + u_align[j:]
        elif backtrack[i][j] == 2: # a deletion
            j -= 1
            r_align = r_align[:i] + '-' + r_align[i:]
        else: # a match
            i -= 1
            j -= 1

    # Prepend insertions/deletions if necessary.
    for dash in range(i):
        u_align = u_align[:0] + '-' + u_align[0:]
    for dash in range(j):
        r_align = r_align[:0] + '-' + r_align[0:]

    return(str(max_score), r_align, u_align)


def main():
    s, t = parse_fasta('problem_datasets/rosalind_loca.txt', True)
    score_matrix = scoring_matrix('data/PAM250.txt')

    alignment = alignment_score(s, t, score_matrix, -5)
    print('\n'.join(alignment))
        

if __name__ == '__main__':
    main()
