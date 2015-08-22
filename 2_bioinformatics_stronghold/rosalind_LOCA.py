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
(note: this is correct, but different than Rosalind sample output):
23
MEANLYPRTEINSTRIN
LEASANTLYEINSTEIN
'''

from rosalind_utils import parse_fasta, scoring_matrix, print_matrix

def get_score(scores, a, b):
    ''' Return the score from the scoring matrix. '''
    x = scores[0].index(a)
    y = scores[0].index(b)
    cost = int(scores[x+1][y])

    return(cost)

    
def alignment_score(s, t, matrix, gap):
    ''' Returns two matrices of the edit distance and edit alignment between
        strings s and t.
    '''

    # Initialize the matrices with zeros.
    d = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    traceback = [[3 for j in range(len(t)+1)] for i in range(len(s)+1)]

    best = 0
    best_pos = (0, 0)

    # Fill in the Score and Traceback matrices.
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            cost = [ d[i-1][j-1] + get_score(matrix, s[i-1], t[j-1]),
                     d[i-1][j] + gap,
                     d[i][j-1] + gap,
                     0 ]
            d[i][j] = max(cost)
            traceback[i][j] = cost.index(d[i][j])

            if d[i][j] >= best:
                best = d[i][j]
                best_pos = (i, j)

    # Optional: Print the score and traceback matrices.
    #print_matrix(d, s, t)
    #print()
    #print_matrix(traceback, s, t)
    #print()

    # Initialize the values of i,j
    i, j = best_pos

    # Initialize the aligned strings as the input strings.
    r, u = s[:i], t[:j]
    
    # Backtrack to the edge of the matrix starting at the bottom right.
    while traceback[i][j] != 3 and i*j != 0:
        if traceback[i][j] == 0: # a match
            i -= 1
            j -= 1
        elif traceback[i][j] == 1: # an insertion
            i -= 1
        elif traceback[i][j] == 2: # a deletion
            j -= 1

    r = r[i:]
    u = u[j:]

    return(str(best), r, u)


def main():
    s, t = parse_fasta('problem_datasets/rosalind_loca.txt', True)
    scores = scoring_matrix('data/PAM250.txt')
    alignment = alignment_score(s, t, scores, -5)

    with open('output/rosalind_loca_out.txt', 'w') as outfile:
        outfile.write('\n'.join(alignment))

    print('\n'.join((alignment[0], alignment[1][:77]+'...', alignment[2][:77]+'...')))


if __name__ == '__main__':
    main()
