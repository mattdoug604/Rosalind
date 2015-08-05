#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Consensus and Profile
URL: http://rosalind.info/problems/cons/

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
'''

from rosalind_utils import parse_fasta
import re

    
def profile_matrix(seqs):
    ''' Generate a profile matrix from a list of DNA sequences. Assumes all the
        sequences are of equal length.
    '''
    length = len(seqs[0])
    matrix =[[0 for x in range(4)] for y in range(length)]
    letters = {'A':0, 'C':1, 'G':2, 'T':3}

    for i in range(length):
        for string in seqs:
            s = string[i]
            matrix[i][letters[s]] += 1

    return(matrix)


def consensus_seq(profile):
    ''' Determine the consensus sequence from a given profile matrix. '''
    consensus = ''
    letter = ['A', 'C', 'G', 'T']
    
    for i in range(len(profile)):
        nt = profile[i].index(max(profile[i]))
        consensus += letter[nt]

    return(consensus)


def format_profile(profile):
    ''' A generator that outputs the profile matrix in a readable format. '''
    prefix = ['A', 'C', 'G', 'T']
    
    for i in range(4):
        line = prefix[i] + ': '
        for j in range(len(profile)):
            line += str(profile[j][i]) + ' '

        yield(line)


def main():
    sequences = list(parse_fasta('problem_datasets/rosalind_cons.txt').values())
    profile = profile_matrix(sequences)
    consensus = consensus_seq(profile)

    with open('output/rosalind_cons_out.txt', 'w') as outfile:
        outfile.write(consensus + '\n')
        for line in format_profile(profile):
            outfile.write(line + '\n')


if __name__ == '__main__':
    main()
