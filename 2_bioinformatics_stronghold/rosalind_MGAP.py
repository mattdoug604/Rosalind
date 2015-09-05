#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Maximizing the Gap Symbols of an Optimal Alignment
URL: http://rosalind.info/problems/mgap/

Given: Two DNA strings s and t in FASTA format (each of length at most 5000 bp).
Return: The maximum number of gap symbols that can appear in any maximum score
alignment of s and t with score parameters satisfying m>0, d<0, and g<0.
'''

'''
EXAMPLE INPUT:
>Rosalind_92
AACGTA
>Rosalind_47
ACACCTA

EXAMPLE OUTPUT:
3
'''

from rosalind_utils import parse_fasta

def max_global_align_gaps(s, t, m=1, d=-1, g=-1):
    
    # Initialize the similarity matrix.
    S = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]

    # Each cell in the first row and column recieves a gap penalty.
    for i in range(1, len(s)+1):
        S[i][0] = i * g
    for j in range(1, len(t)+1):
        S[0][j] = j * g

    # Fill in the similarity matrix.
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            scores = [S[i-1][j-1] + (m if s[i-1] == t[j-1] else d),
                      S[i-1][j] + g,
                      S[i][j-1] + g]
            S[i][j] = max(scores)
    
    # The max possible score is the last cell of the similarity matrix.
    return S[-1][-1]

   
def main():
    s, t = parse_fasta('problem_datasets/rosalind_mgap.txt')

    print(max_global_align_gaps(s, t))
        

if __name__ == '__main__':
    main()
