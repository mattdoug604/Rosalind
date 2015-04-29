#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: RNA Splicing
URL: http://rosalind.info/problems/splc/

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.
Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)
'''

from rosalind_functions import parseFasta, codonTable

def translate(string):
    ''' rosalind problems sometimes have 'rna' sequences with thymine in them '''
    codons = codonTable()
    peptide = ''
    
    ''' translate the rna sequence '''
    for nt in range(0, len(string), 3):
        codon = string[nt:nt+3]
        aa = codons.get(codon, '*')
        if aa != '*':
            peptide += aa
        else:
            break
    if peptide != '':
        return(peptide)
    else:
        return('No exon found.')

def spliceRNA(rna, introns):
    for i in introns:
        rna = rna.replace(i, '')
        
    return(rna)

def main():
    sequences = parseFasta('problem_datasets/rosalind_splc.txt')
    rna = max(sequences.values(), key=len)
    introns = [i for i in sequences.values() if i != rna]

    spliced = spliceRNA(rna, introns)
    peptide = translate(spliced)
    with open('output/rosalind_splc_out.txt', 'w') as outfile:
        outfile.write(peptide)

if __name__ == '__main__':
    main()
