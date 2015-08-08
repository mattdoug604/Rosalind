#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Edit Distance Alignment
URL: http://rosalind.info/problems/edta/

Given: Two protein strings s and t in FASTA format (with each string having length at most 1000 aa).
Return: The edit distance dE(s,t) followed by two augmented strings s′ and t′ representing an optimal alignment of s and t.
'''

'''
EXAMPLE INPUT:
>Rosalind_43
PRETTY
>Rosalind_97
PRTTEIN

EXAMPLE OUTPUT:
4
PRETTY--
PR-TTEIN
'''

from rosalind_utils import parse_fasta

def print_matrix(matrix, s, t):
    ''' Optional: Write out the distance matrix. '''
    print('Writing matrix...\n')
    print('     ' + ' '.join(t))
    for x, m in enumerate(matrix):
        if x > 0:
            line = s[x-1] +' [' + ' '.join(map(str, m)) + ']'
        else:
            line = '  [' + ' '.join(map(str, m)) + ']'
        print(line)
    print()


def build_matrices(s, t):
    ''' Returns two matrices of the edit distance and edit alignment between
        strings s and t.
    '''

    # Initialize the matrices with zeros.
    d = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    backtrack = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    
    for i in range(1, len(s)+1):
        d[i][0] = i
    for j in range(1, len(t)+1):
        d[0][j] = j

    # Fill in the Distance and Backtrack matrices.
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            scores = [d[i-1][j-1] + (s[i-1] != t[j-1]), d[i-1][j]+1, d[i][j-1]+1]
            d[i][j] = min(scores)
            backtrack[i][j] = scores.index(d[i][j]) # 0=match, 1=insertion, 2=deletion

    return(d, backtrack)


def align_sequences(s, t):
    distance, backtrack = build_matrices(s, t)

    #print_matrix(distance, s, t)
    #print_matrix(backtrack, s, t)

    # The edit distance is found at the bottom corner of the Score matrix.
    edit_dist = distance[-1][-1]
    
    # Initialize the aligned strings as the input strings.
    s_align, t_align = s, t

    # Initialize the values of i,j
    i, j = len(s), len(t)

    # Backtrack to the edge of the matrix starting at the bottom right.
    while i>0 and j>0:
        if backtrack[i][j] == 1: # an insertion
            i -= 1
            t_align = t_align[:j] + '-' + t_align[j:]
        elif backtrack[i][j] == 2: # a deletion
            j -= 1
            s_align = s_align[:i] + '-' + s_align[i:]
        else: # a match
            i -= 1
            j -= 1

    # Prepend insertions/deletions if necessary.
    for dash in range(i):
        t_align = t_align[:0] + '-' + t_align[0:]
    for dash in range(j):
        s_align = s_align[:0] + '-' + s_align[0:]

    return str(edit_dist), s_align, t_align

   
def main():
    s, t = parse_fasta('problem_datasets/rosalind_edta.txt', 'seq')
    aligned = align_sequences(s, t)

    with open('output/rosalind_edta_out.txt', 'w') as outfile:
        outfile.write('\n'.join(aligned))
        print('Edit distance =', aligned[0])
        

if __name__ == '__main__':
    main()
