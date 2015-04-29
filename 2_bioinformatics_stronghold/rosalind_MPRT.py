#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Finding a Protein Motif
URL: http://rosalind.info/problems/mprt/

Given: At most 15 UniProt Protein Database access IDs.
Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.
'''

from urllib2 import urlopen
import re

def parseSequence(fasta):
    ''' Takes a FASTA formated sequence retrieved from uniprot and
        returns only the protein sequence.
    '''
    seq = re.sub('^\>(.*)\n', '', fasta, 1)
    seq = seq.replace('\n', '')
    return(seq)

def findMotifs(seq_list, pattern):
    ''' Idetnifies the position(s) of a given motif in each of the
        protein sequences. Returns a dicitonary containing the IDs and
        corresponding motif locations. Sequences with no found motifs 
        are ommitted.
    '''
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
    ''' Reads a text file of UniProt access IDs (seperated by new-lines),
        retrieves the protein sequences from UniProt, and identifies any
        N-glycoslyation motifs
    '''
    pattern = '^N[A-O,Q-Z](S|T)[A-O,Q-Z]'
    
    with open('problem_datasets/rosalind_mprt.txt', 'r') as infile:
        ids = infile.read().strip().split('\n')

    fastas = {}
    for i in ids:
        site = 'http://www.uniprot.org/uniprot/' + i + '.fasta'
        html = urlopen(site).read()
        seq = parseSequence(html)
        fastas[i] = seq

    with open('output/rosalind_mprt_out.txt', 'w') as outfile:
        for key, val in findMotifs(fastas, pattern):
            outfile.write(key + '\n' + val + '\n')
    
if __name__ == '__main__':
    main()
