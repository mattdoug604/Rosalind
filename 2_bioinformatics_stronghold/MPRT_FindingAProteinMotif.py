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

def parseFasta(file_name, ids):
    ''' Reads a text file containing 1 or more fasta sequences,
        returns a dictionary of all the seperate sequences '''
    heads = []
    seqs = {}

    with open(file_name, 'r') as f:
        for num, line in enumerate(f):
            if '>' in line:
                heads.append(num)
    heads.append(sum(1 for line in open(file_name)))

    f = open(file_name, 'r')
    lines = f.readlines()
    for i in range(len(heads)-1):
        h = ids[i]
        #h = lines[heads[i]].replace('\n', '')
        l = lines[heads[i]+1:heads[i+1]]
        seqs[h] = ''.join(l).replace('\n', '')

    return seqs


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
    
    with open('rosalind_mprt.txt', 'r') as infile:
        ids = infile.read().strip().split('\n')
    '''
    with open('rosalind_mprt_out.txt', 'w') as outfile:
        for i in ids:
            site = 'http://www.uniprot.org/uniprot/' + i + '.fasta'
            html = urlopen(site).read()
            outfile.write(html)

        sequences = parseFasta(outfile)
    '''
    sequences = parseFasta('rosalind_mprt_out.txt', ids)
    for key, val in findMotifs(sequences, pattern):
        print(key + '\n' + val)

if __name__ == '__main__':
    main()
