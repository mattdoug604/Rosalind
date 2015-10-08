#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Wobble Bonding and RNA Secondary Structures
URL: http://rosalind.info/problems/rnas/

Given: An RNA string s (of length at most 200 bp).

Return: The total number of distinct valid matchings of basepair edges in the
 bonding graph of s. Assume that wobble base pairing is allowed.

'''

def pair(seq):
    ''' Return the number of noncrossing matchings of basepair edges. ''' 
    # Only one possible match for a seq of length one.
    if len(seq) <= 1:
        return 1
    
    # No need to recalculate a sequence if we've already done so.
    if seq in prev:
        return prev[seq]
    # Otherwise, do the calculation and add it to the dictionary.
    else: 
        prev[seq] = pair(seq[1:])
        
        for i in range(3, len(seq)):
            if seq[i] == match[seq[0]]:
                prev[seq] += pair(seq[1:i]) * pair(seq[i+1:])
    
    return prev[seq]
    
    
if __name__ == '__main__':
    match = {'A':'U','U':'A', 'C':'G', 'G':'C', 'G':'U', 'U':'G'}
    prev = {}
    
    with open('problem_datasets/rosalind_rnas.txt', 'r') as infile:
        seq = infile.read().replace('\n', '')
    
    #print(pair(seq))
    
    cor = 284850219977421
    ans = pair(seq)
    if ans == cor:
        print('Yes!', ans)
    elif abs(ans - cor) < 10:
        print(ans, 'diff =', ans - cor)
    else:
        print(ans)
    