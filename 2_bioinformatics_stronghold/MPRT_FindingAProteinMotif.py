#!/usr/bin/python
# MPRT_FindingAProteinMotif.py

'''
Given: At most 15 UniProt Protein Database access IDs.
Return: For each protein possessing the N-glycosylation motif,
    output its given access ID followed by a list of locations
    in the protein string where the motif can be found.

N-glycosylation motif is denoted by: N{P}[ST]{P}, where [ST]
means "either S or T" and {P} means "any except P"
'''

import urllib.request
import re

def parseFasta(fasta_list):
    ''' Takes a dictionary of UniProt IDs w/ associated
        data in FASTA format, and returns a new dictionary
        of IDs w/ corresponding DNA sequences '''
    sequences = {}

    for f in fasta_list:
        seq = ''.join(fasta_list[f].strip().split('\n')[1:])
        sequences[f] = seq

    return(sequences)


def findMotifs(seq_list, pattern):
    pattern = re.compile(pattern)
    results = {}

    for i in seq_list:
        index = []
        name = i
        seq = seq_list[name]
        
        for j in range(len(seq)):
            if pattern.match(seq[j:j+4]):
                index.append(str(j+1))
        
        if len(index) != 0:
            results[name] = ' '.join(index)

    return(sorted(results.items()))

def main():
    ''' Reads a text file of UniProt access IDs (seperated by newlines),
        retrieves the protein sequences from UniProt, and identifies any
        N-glycoslyation motifs '''
    
    pattern = '^N[A-O,Q-Z](S|T)[A-O,Q-Z]'
    
    with open('problem_datasets/rosalind_mprt.txt', 'r') as infile:
        ids = infile.read().strip().split('\n')

    fastas = {}    
    for i in ids:
        url = 'http://www.uniprot.org/uniprot/' + i + '.fasta'
        html = urllib.request.urlopen(url).read()
        fastas[i] = html.decode('ascii')

    sequences = parseFasta(fastas)
    
    for key, val in findMotifs(sequences, pattern):
        print(key + '\n' + val)

if __name__ == '__main__':
    main()
