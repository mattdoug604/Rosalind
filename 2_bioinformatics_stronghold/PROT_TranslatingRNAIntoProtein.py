#!/usr/bin/python
# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
# Return: The protein string encoded by s.

# create a codon table dictionary
bases = ["U", "C", "A", "G"]
amino_acids = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
codons = [a+b+c for a in bases for b in bases for c in bases]
codon_table = dict(zip(codons, amino_acids))
print codon_table

# read rna sequence from file
rna = open("rosalind_prot.txt")
s = rna.read()
peptide = ""

for nt in range(0, len(s), 3):
    codon = s[nt:nt+3]
    aa = codon_table.get(codon, '*')
    if aa != '*':
        peptide += aa
    else:
        break

print peptide
