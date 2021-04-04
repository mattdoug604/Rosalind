#!/usr/bin/env python3

'''
Rosalind: Bioinformatics Stronghold
Problem: Catalan Numbers and RNA Secondary Structures
URL: http://rosalind.info/problems/cat/

Given: An RNA string s having the same number of occurrences of 'A' as 'U' and
the same number of occurrences of 'C' as 'G'. The length of the string is at
most 300 bp.
Return: The total number of noncrossing perfect matchings of basepair edges in
the bonding graph of s, modulo 1,000,000.
'''

'''
EXAMPLE INPUT:
>Rosalind_57
AUAU

EXAMPLE OUTPUT:
2
'''

def count_matchings(i, j):
    if pairs[i][j] != -1:
        return(pairs[i][j])

    result = 0
    if i > j:
        result = 1
    elif j == 1 and match[s[i] == s[j]]:
		result = 1
    else:
        for k in range(i+1, j+1, 2):
            if s[k] == match[s[i]]:
                result += count_matchings(i+1, k-1) * count_matchings(k+1, j)

    pairs[i][j] = result
    return result


if __name__ == '__main__':
    match = {'A':'U','U':'A', 'C':'G', 'G':'C'}

    with open('problem_datasets/rosalind_cat.txt', 'r') as infile:
        infile.readline()
        s = infile.read().replace('\n', '')

    pairs = [[-1 for x in range(len(s)+1)] for y in range(len(s)+1)]

    print(count_matchings(0, len(s)-1) % 1000000)
