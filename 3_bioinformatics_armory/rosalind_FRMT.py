#!/usr/bin/python

'''
Rosalind: Bioinformatics Armory
Problem: Data Formats
URL: http://rosalind.info/problems/frmt/

Given: A collection of n (n <= 10) GenBank entry IDs.
Return: The shortest of the strings associated with the IDs in FASTA format.
'''

from Bio import Entrez
from Bio import SeqIO

def main():
    Entrez.email = input('Please specify an email address for the NCBI database:\n').strip()
            
    # Read the GerBank IDs from a text file.
    with open('problem_datasets/rosalind_frmt.txt', 'r') as infile:
        gen_ids = infile.read().strip().split()

    # Retrieve the plain text records in FASTA format from the NCBI database.
    handle = Entrez.efetch(db='nucleotide', id=gen_ids, rettype='fasta')
    
    # Parse the records into a useable list.
    records = list(SeqIO.parse(handle, 'fasta'))
    
    # Find the shortest sequence.
    min_seq = min(records, key=lambda i: len(i.seq))
    
    # Output the answer.
    with open('output/rosalind_frmt_out.txt', 'w') as outfile:
        SeqIO.write(min_seq, outfile, 'fasta')

    # Optional: Print answer and gene ID/name
    print('\nThe shortest sequence is: %s' % min_seq.id)
    
    
if __name__ == '__main__':
    main()
