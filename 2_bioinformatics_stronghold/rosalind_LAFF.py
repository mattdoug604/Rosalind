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
    
    # Initialize the matrices (short).
    Sx = [0 for i in range(len(t)+1)]
    Sy = [0 for j in range(len(t)+1)]
    Sm = [0 for i in range(len(t)+1)]
    traceback = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    
    best = -1
    best_pos = (0, 0)

    # Fill in the Score and Traceback matrices.
    for i in range(1, len(s)+1):
        new_x = [0 for i in range(len(t)+1)]
        new_y = [0 for i in range(len(t)+1)]
        new_m = [0 for i in range(len(t)+1)]
        
        for j in range(1, len(t)+1):
            new_x[j] = max([Sm[j] + gap,
                            Sx[j] + gap_e])
            new_y[j] = max([new_m[j-1] + gap,
                         new_y[j-1] + gap_e])
            costM = [Sm[j-1] + get_score(scores, s[i-1], t[j-1]),
                     new_x[j],
                     new_y[j],
                     0]
            new_m[j] = max(costM)
            traceback[i][j] = costM.index(new_m[j])

            if new_m[j] > best:
                best = new_m[j]
                best_pos = i, j

        Sx = new_x
        Sy = new_y
        Sm = new_m
    
    # Initialize the values of i,j
    i, j = best_pos
    
    # Initialize the aligned strings as the input strings.
    r, u = s[:i], t[:j]

    # Traceback to build alignment.
    while traceback[i][j] != 3 and i*j != 0:
        if traceback[i][j] == 0:
            i -= 1
            j -= 1
        elif traceback[i][j] == 1:
            i -= 1
        elif traceback[i][j] == 2:
            j -= 1
   
    r = r[i:]
    u = u[j:]
    
    return(str(best), r, u)


def main():
    s, t = parse_fasta('problem_datasets/rosalind_laff.txt', True)
    scores = scoring_matrix('data/BLOSUM62.txt')

    alignment = alignment_score(s, t, scores, -11, -1)
    print('Maximum alignment score =', alignment[0])
    with open('output/rosalind_laff_out.txt', 'w') as outfile:
        outfile.write('\n'.join(alignment))


if __name__ == '__main__':
    main()
