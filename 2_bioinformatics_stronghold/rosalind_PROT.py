#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Translating RNA into Protein
URL: http://rosalind.info/problems/prot/

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
Return: The protein string encoded by s.
'''

from rosalind_functions import codonTable

def main():
    codon_table = codonTable('rna')

    with open('problem_datasets/rosalind_prot.txt', 'r') as infile:
        rna = infile.read().strip()

    peptide = ''
    for nt in range(0, len(rna), 3):
        codon = rna[nt:nt+3]
        aa = codon_table.get(codon, '*')
        if aa != '*':
            peptide += aa
        else:
            break

    with open('output/rosalind_prot_out.txt', 'w') as outfile:
        print(peptide)
        outfile.write(peptide)

if __name__ == '__main__':
    main()
