#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Consensus and Profile
URL: http://rosalind.info/problems/cons/

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
'''

import re

def parseFasta(path):
    ''' Read a single file containing multiple
        FASTA sequences, extract only the DNA
        sequences, and split them into seperate
        strings.
    '''
    seqs = ''
    with open(path, 'r') as fasta:
        for line in fasta:
            if not re.search(r'^>.+$\n', line):
                seqs += line.strip()
            else:
                seqs += '\n'
    
    seqs = seqs.lstrip().split('\n')
    return(seqs)
    
def profileMatrix(seqs):
    ''' Generate a profile matrix from a list of
        DNA sequences. Assumes all the sequences
        are of equal length.
    '''
    length = len(seqs[0])
    matrix =[[0 for x in range(4)] for y in range(length)]
    
    for i in range(length):
        for string in seqs:
            if string[i].upper() == 'A':
                matrix[i][0] += 1
            elif string[i].upper() == 'C':
                matrix[i][1] += 1
            elif string[i].upper() == 'G':
                matrix[i][2] += 1
            elif string[i].upper() == 'T':
                matrix[i][3] += 1

    return(matrix)

def consensusSeq(profile):
    ''' Determine the consensus sequence from a
        given profile matrix.
    '''
    consensus = ''

    letter = ['A', 'C', 'G', 'T']
    for i in range(len(profile)):
        nt = profile[i].index(max(profile[i]))
        consensus += letter[nt]

    return(consensus)

def formatProfile(profile):
    ''' A generator that outputs a given profile
        matrix in a readable format.
    '''
    prefix = ['A', 'C', 'G', 'T']
    for i in range(4):
        line = prefix[i] + ': '
        for j in range(len(profile)):
            line += str(profile[j][i]) + ' '

        yield(line)

def main():
    sequences = parseFasta('problem_datasets/rosalind_cons.txt')
    profile = profileMatrix(sequences)
    consensus = consensusSeq(profile)

    with open('output/rosalind_cons_out.txt', 'w') as outfile:
        outfile.write(consensus + '\n')
        for line in formatProfile(profile):
            outfile.write(line + '\n')

if __name__ == '__main__':
    main()
