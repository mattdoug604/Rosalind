#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Catalan Numbers and RNA Secondary Structures 
URL: http://rosalind.info/problems/cat/

Given: An RNA string s having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'. The length of the string is at most 300 bp.
Return: The total number of noncrossing perfect matchings of basepair edges in the bonding graph of s, modulo 1,000,000.
'''

'''
EXAMPLE INPUT:
>Rosalind_57
AUAU

EXAMPLE OUTPUT:
2
'''

def count_matchings(i, j):
    ''' Calculate the total number of noncrossing basepairs, modulo a million,
        for a string of DNA with the same number of occurances of 'A' as 'T'
        and 'C' as 'G'.
    ''' 
    if pairs[i][j] != -1:
        print('cond #1', i, j)
        return(pairs[i][j])

    sub = s[i:j+1]
    
    result = 0
    if i > j:
        print('cond #2', i, j)
        result = 1
    elif j == 1 and match[s[i] == s[j]]:
        print('cond #3', i, j)
        result = 1
    else:
        print('cond #4', i, j)
        result = sum([(count_matchings(i+1, k-1) * count_matchings(k+1, j))
                      for k in range(i+1, j+1, 2)
                      if match[s[i]] == s[k]])

    print('-> cond #5', i, j)
    pairs[i][j] = result
    return(result)

    
if __name__ == '__main__':
    with open('problem_datasets/rosalind_cat.txt', 'r') as infile:
        next(infile)
        s = infile.read().replace('\n', '')
        
    s = 'AUCGAU'
    pairs = [[-1 for x in range(len(s)+1)] for y in range(len(s)+1)]
    match = {'A':'U','U':'A', 'C':'G', 'G':'C'}
    
    print(count_matchings(0, len(s)-1) % 1000000)

    for p in pairs:
        print(p)