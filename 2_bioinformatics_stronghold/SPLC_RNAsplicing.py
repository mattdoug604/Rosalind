#!/usr/bin/python
# SPLC_RNAsplicing.py

'''
Given: A DNA string s (of length at most 1 kbp) and a collection of substrings
    of s acting as introns. All strings are given in FASTA format.
Return: A protein string resulting from transcribing and translating the exons
    of s. (Note: Only one solution will exist for the dataset provided.)
'''

from rosalind_functions import parseFasta, codonTable

def translate(string):
    ''' rosalind problems sometimes have 'rna' sequences with thymine in them '''
    rna = string.replace('T', 'U')

    codons = codonTable()
    peptide = ''
    
    ''' translate the rna sequence '''
    for nt in range(0, len(rna), 3):
        codon = rna[nt:nt+3]
        aa = codons.get(codon, '*')
        if aa != '*':
            peptide += aa
        else:
            break

    return(peptide)

def spliceRNA(rna, introns):
    for i in introns:
        rna = rna.replace(i, '')
        
    return(rna)

def main():
    sequences = parseFasta('rosalind_splc.txt')
    rna = max(sequences.values(), key=len)
    introns = [i for i in sequences.values() if i != rna]

    spliced = spliceRNA(rna, introns)
    peptide = translate(spliced)
    print(peptide)

if __name__ == '__main__':
    main()
