#!/usr/bin/env python3

'''
Rosalind: Bioinformatics Stronghold
Problem: Transcribing DNA into RNA
URL: http://rosalind.info/problems/rna/

Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
'''

def transcribe():
    with open('problem_datasets/rosalind_rna.txt', 'r') as infile:
        dna = ''.join(infile.read().strip())

    rna = dna.replace('T', 'U')
    
    with open('output/rosalind_rna_out.txt', 'w') as outfile:
        outfile.write(rna)


if __name__ == '__main__':
    transcribe()
