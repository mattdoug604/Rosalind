#!/usr/bin/env python3

'''
Rosalind: Bioinformatics Stronghold
Problem: Counting Optimal Alignments
URL: http://rosalind.info/problems/ctea/

Given: Two protein strings s and t in FASTA format, each of length at most 1000
aa.
Return: The total number of optimal alignments of s and t with respect to edit
alignment score, modulo 134,217,727 (227-1).
'''

'''
EXAMPLE INPUT:
>Rosalind_78
PLEASANTLY
>Rosalind_33
MEANLY

EXAMPLE OUTPUT:
4
'''

from rosalind_utils import parse_fasta

def count_alignments(s, t):
    ''' Calculate the minimum edit distance between two strings, s and t, and
        the number of alignments with that score, modulo 2^27 - 1.
    '''

    # Initialize the distance and alignment count matrices with zeros.
    d = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    counts = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    
    # Each cell in the first row and column of the distance matrix recieves a
    # gap penalty (-1) after the first. Similarily, each cell of the count
    # matrix starts as 1.
    for i in range(0, len(s)+1):
        d[i][0] = i
        counts[i][0] = 1
    for j in range(1, len(t)+1):
        d[0][j] = j
        counts[0][j] = 1
    
    # Fill in the matrices.
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            scores = [d[i-1][j-1] + (s[i-1] != t[j-1]),
                      d[i-1][j] + 1,
                      d[i][j-1] + 1]
            d[i][j] = min(scores)

            # If the score matches the minimum, add the preceeding number of
            # alignments.
            if d[i][j] == scores[0]: counts[i][j] += counts[i-1][j-1]
            if d[i][j] == scores[1]: counts[i][j] += counts[i-1][j]
            if d[i][j] == scores[2]: counts[i][j] += counts[i][j-1]

            # Take the count modulo 2**27 - 1.
            counts[i][j] = counts[i][j] % 134217727
    
    return counts[-1][-1]


def main():
    # Read in the two input strings.
    s, t = parse_fasta('problem_datasets/rosalind_ctea.txt')

    # Print the number of optimal alignments (modulo 2^27 - 1).
    print(count_alignments(s, t))


if __name__ == '__main__':
    main()
