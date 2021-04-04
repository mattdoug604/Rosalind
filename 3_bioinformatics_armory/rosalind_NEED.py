#!/usr/bin/env python3

'''
Rosalind: Bioinformatics Armory
Problem: Pairwise Global Alignment
URL: http://rosalind.info/problems/need/

Given: Two GenBank IDs.
Return: The maximum global alignment score between the DNA strings associated 
with these IDs.
'''

from time import time

import subprocess
from Bio import Entrez
from Bio import SeqIO
import Bio.Emboss.Applications

def main():
    Entrez.email = input('Please specify an email address for the NCBI database:\n').strip()
    
    # Read in two GenBank IDs.
    with open('problem_datasets/rosalind_need.txt', 'r') as infile:
        gen_ids = infile.read().strip().split(' ')
    
    # Retrieve the plain text records in FASTA format from the NCBI database.
    handle = Entrez.efetch(db='nucleotide', id=gen_ids, rettype='fasta')
    
    # Parse the records into a useable list.
    records = list(SeqIO.parse(handle, 'fasta'))
    
    # Output fasta files.
    for i, record in enumerate(records):
        out_handle = 'output/temp' + str(i) + '.fasta'
        SeqIO.write(record, out_handle, 'fasta')
        
    # Get needle output.
    pair = Bio.Emboss.Applications.NeedleCommandline('output\temp1.fasta')
    print(pair)
    

if __name__ == '__main__':
    start = time()
    main()
    print('\nRuntime =', time()-start, 'seconds.')
