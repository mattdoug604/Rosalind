#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Finding All Similar Motifs
URL: http://rosalind.info/problems/ksim/

Given: A positive integer k (k≤50), a DNA string s of length at most 5 kbp 
representing a motif, and a DNA string t of length at most 50 kbp representing
 a genome.

Return: All substrings t′ of t such that the edit distance dE(s,t′) is less 
than or equal to k. Each substring should be encoded by a pair containing its 
location in t followed by its length.
'''

from rosalind_utils import print_matrix

def edit_distance(k, s, t):
    m = len(s) + 1
    n = len(t) + 1
    
    lengths = []
    
    # Initialize the distance matrix with zeros.
    d = [[0 for j in range(n)] for i in range(m)]

    # Each cell in the first row and column counts as an edit.
    for i in range(1, m):
        d[i][0] = i
    for j in range(1, n):
        d[0][j] = j

    # Fill in the distance matrix.
    for i in range(1, m):
        for j in range(1, n):
            scores = [d[i-1][j-1] + (s[i-1] != t[j-1]), # 0 = match
                      d[i-1][j] + 1,                    # 1 = insertion
                      d[i][j-1] + 1]                    # 2 = deletion
            d[i][j] = min(scores)
    
            if i == m-1 and d[i][j] <= k:
                lengths.append(j)
    
    print_matrix(d, s, t)  
    
    return lengths
    

def modified_motifs(k, s, t):
    pairs = [(1, i) for i in edit_distance(k, s, t)]
        
    return pairs
    
    
def main():
    with open('problem_datasets/rosalind_ksim.txt', 'r') as infile:
        k = int(infile.readline())
        s, t = infile.read().strip().split('\n')
        
    k, s, t = 2, 'ACGTAG', 'ACGGATCGGCATCGT'
        
    print('len(s)='+str(len(s)), 'len(t)='+str(len(t)))
    
    print('\n'.join([' '.join(map(str, i)) for i in modified_motifs(k, s, t)]))


if __name__ == '__main__':
    main()
    
# INPUT:
# 2
# ACGTAG
# ACGGATCGGCATCGT
#    
# OUTPUT:
# 1 4 <- ACGTAG
#        ACG--G
# 1 5 <- ACGTAG
#        ACGGA-
# 1 6 <- ACGTAG
#        ACGGAT