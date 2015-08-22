#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Local Alignment with Affine Gap Penalty
URL: http://rosalind.info/problems/laff/

Given: Two protein strings s and t in FASTA format (each having length at most 10,000 aa).
Return: The maximum local alignment score of s and t, followed by substrings r and u of s and t, respectively, that correspond to the optimal local alignment of s and t. Use:
    The BLOSUM62 scoring matrix.
    Gap opening penalty equal to 11.
    Gap extension penalty equal to 1.
If multiple solutions exist, then you may output any one.
'''

'''
EXAMPLE INPUT:
>Rosalind_8
PLEASANTLY
>Rosalind_18
MEANLY

EXAMPLE OUTPUT:
12
LEAS
MEAN
'''

from rosalind_utils import parse_fasta, scoring_matrix

def get_score(scores, a, b):
    ''' Return the score from the scoring matrix. '''
    x = scores[0].index(a)
    y = scores[0].index(b)
    cost = int(scores[x+1][y])

    return(cost)

    
def alignment_score(s, t, scores, gap, gap_e):
    ''' Returns two matrices of the edit distance and edit alignment between
        strings s and t.
    '''

    # Initialize the matrices. 
    Sx = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    Sy = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    Sm = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]

    traceX = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    traceY = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    traceM = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    
    best = -9999
    best_pos = (0, 0, 0)

    # Fill in the Score and Traceback matrices.
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            costX = [Sm[i-1][j] + gap,
                     Sx[i-1][j] + gap_e]
            Sx[i][j] = max(costX)
            traceX[i][j] = costX.index(Sx[i][j])
            
            costY = [Sm[i][j-1] + gap,
                     Sy[i][j-1] + gap_e]
            Sy[i][j] = max(costY)
            traceY[i][j] = costY.index(Sy[i][j])

            costM = [Sm[i-1][j-1] + get_score(scores, s[i-1], t[j-1]),
                     Sx[i][j],
                     Sy[i][j]]
            Sm[i][j] = max(costM)
            traceM[i][j] = costM.index(Sm[i][j])

            new = Sx[i][j], Sy[i][j], Sm[i][j]
            best_new = max(new)
            if best_new >= best:
                best = best_new
                best_pos = (new.index(best), i, j)

    # Initialize the values of i,j
    lvl, i, j = best_pos

    # Initialize the aligned strings as the input strings.
    r, u = s[:i], t[:j]
    
    # Traceback to build alignment.
    while i>0 and j>0:
        if lvl == 0:
            if traceX[i][j] == 0:
                lvl = 2
            i -= 1

        elif lvl == 1:
            if traceY[i][j] == 0:
                lvl = 2
            j -= 1

        elif lvl == 2:
            if traceM[i][j] == 1:
                lvl = 0
            elif traceM[i][j] == 2:
                lvl = 1
            else:
                i -= 1
                j -= 1

    r = r[i:]
    u = u[j:]

    return(str(best), r, u)


def main():
    s, t = parse_fasta('problem_datasets/rosalind_laff.txt', True)
    print(len(s), len(t))
    #s, t = ('PLEASANTLY', 'MEANLY')
    scores = scoring_matrix('data/BLOSUM62.txt')
    
    alignment = alignment_score(s, t, scores, -11, -1)
    #print('\n'.join(alignment))
    with open('output/rosalind_laff_out.txt', 'w') as outfile:
        outfile.print('\n'.join(alignment))


if __name__ == '__main__':
    main()
