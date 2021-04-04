#!/usr/bin/env python3

'''
Rosalind: Bioinformatics Stronghold
Problem: Maximizing the Gap Symbols of an Optimal Alignment
URL: http://rosalind.info/problems/mgap/

Given: Two DNA strings s and t in FASTA format (each of length at most 5000 bp).

Return: The maximum number of gap symbols that can appear in any maximum score
alignment of s and t with score parameters satisfying m>0, d<0, and g<0.
'''

from rosalind_utils import parse_fasta

def global_align_max_gaps(s, t):
    # Initialize two matrices, one to hold the score and one to count the gaps.
    S = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    gaps = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    
    # Cells in the first row and column of each matrix count as a gap.
    for i in range(1, len(s)+1):
        S[i][0] = -i
        gaps[i][0] = i
    for j in range(1, len(t)+1):
        S[0][j] = -j
        gaps[0][j] = j

    # Find the maximum alignment score, but make the cost of a mismatch 
    # outrageously high so the creation of a gap will occur whenever there is 
    # not a match.
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            scores = [S[i-1][j-1] + (1 if s[i-1] == t[j-1] else -10**5),
                      S[i-1][j] - 1,
                      S[i][j-1] - 1]
            S[i][j] = max(scores)
            
            # Keep track of each new gap that is created.
            if S[i][j] == scores[0]: 
                gaps[i][j] = gaps[i-1][j-1]
            elif S[i][j] == scores[1]: 
                gaps[i][j] = gaps[i-1][j] + 1
            elif S[i][j] == scores[2]: 
                gaps[i][j] = gaps[i][j-1] + 1
    
    # Return the number of gaps in the optimal alignment.
    return gaps[-1][-1]

   
def main():
    s, t = parse_fasta('problem_datasets/rosalind_mgap.txt')
    
    print(max_global_align_gaps(s, t))
        

if __name__ == '__main__':
    main()
