#!/usr/bin/python

# Translate an RNA string into an amino acid string.
# Given: An RNA string Pattern.
# Return: The translation of Pattern into an amino acid string Peptide.

def getCodonTable():
    '''
    Generates an RNA codon table in dictionary form.
    Note: STOP codons denoted with an asterisk (*)
    '''
    aa = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    bases = ['U','C','A','G']
    codons = [a+b+c for a in bases for b in bases for c in bases]
    codon_table = dict(zip(codons, aa))

    return codon_table

with open('rosalind_2a.txt', 'r') as infile:
    rna = infile.read()

# Translate RNA sequence
codons = getCodonTable()
peptide = ''
for i in range(0, len(rna), 3):
    codon = rna[i:i+3]
    if codons[codon] != '*':
        peptide += codons[codon]
    else:
        break

print(peptide)
