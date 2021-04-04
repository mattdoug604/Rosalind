#!/usr/bin/env python3
"""
Translate an RNA string into an amino acid string.
Given: An RNA string Pattern.
Return: The translation of Pattern into an amino acid string Peptide.
"""
from os.path import dirname, join

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_2a.txt")


def getCodonTable():
    """
    Generates an RNA codon table in dictionary form.
    Note: STOP codons denoted with an asterisk (*)
    """
    aa = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
    bases = ["U", "C", "A", "G"]
    codons = [a + b + c for a in bases for b in bases for c in bases]
    codon_table = dict(list(zip(codons, aa)))

    return codon_table


with open(INPUT_FILE, "r") as infile:
    rna = infile.read()

# Translate RNA sequence
codons = getCodonTable()
peptide = ""
for i in range(0, len(rna), 3):
    codon = rna[i : i + 3]
    if codons[codon] != "*":
        peptide += codons[codon]
    else:
        break

print(peptide)
