#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Translating RNA into Protein
URL: http://rosalind.info/problems/prot/

Given: An RNA string s corresponding to a strand of mRNA (of length at most
10kbp).
Return: The protein string encoded by s.
"""

from rosalind_utils import codon_table


def translate(rna):
    table = codon_table("rna")
    peptide = ""

    for nt in range(0, len(rna), 3):
        codon = rna[nt : nt + 3]
        aa = table.get(codon, "*")
        if aa != "*":
            peptide += aa
        else:
            break

    return peptide


def main():
    with open("problem_datasets/rosalind_prot.txt", "r") as infile:
        rna = infile.read().strip()

    answer = translate(rna)

    with open("output/rosalind_prot_out.txt", "w") as outfile:
        outfile.write(answer)


if __name__ == "__main__":
    main()
