#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Finding a Shared Motif
URL: http://rosalind.info/problems/lcsm/

Given: A collection of k (k <= 100) DNA strings of length at most 1 kbp each in FASTA format.
Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
'''

from rosalind_utils import parse_fasta

def longest_motif(seq_list):
    ''' Finds the longest common substring (motif) from all the sequences.
        Note: the script only returns the *first* motif it finds
    '''
    first_seq = min(seq_list, key=len)
    k = len(first_seq)
    
    for i in range(k, 1, -1):
        for j in range(k-i+1):
            motif = first_seq[j:j+i]
            found = 1
            
            for seq in seq_list:
                s = seq.find(motif)
                if s == -1:
                    found = 0
                    break

            if found == 1:
                return(motif)

    return('no common substring found')
            

def main():
    sequences = list(parse_fasta('problem_datasets/rosalind_lcsm.txt').values())

    answer = longest_motif(sequences)
    print(answer)

if __name__ == '__main__':
    main()
