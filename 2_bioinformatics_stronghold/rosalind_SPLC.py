#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: RNA Splicing
URL: http://rosalind.info/problems/splc/

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings
of s acting as introns. All strings are given in FASTA format.
Return: A protein string resulting from transcribing and translating the exons
of s. (Note: Only one solution will exist for the dataset provided.)
"""

from utils import codon_table, parse_fasta


def translate(string):
    codons = codon_table("dna")
    peptide = ""

    # Translate the rna sequence.
    for nt in range(0, len(string), 3):
        codon = string[nt : nt + 3]
        aa = codons.get(codon, "*")
        if aa != "*":
            peptide += aa
        else:
            break

    return peptide


def splice_RNA(rna, introns):
    for i in introns:
        rna = rna.replace(i, "")

    return rna


def main():
    sequences = parse_fasta("problem_datasets/rosalind_splc.txt")
    rna = max(sequences, key=len)
    introns = [i for i in sequences if i != rna]

    spliced = splice_RNA(rna, introns)
    peptide = translate(spliced)

    if peptide == "":
        print("No exon found.")
    else:
        with open("output/rosalind_splc_out.txt", "w") as outfile:
            outfile.write(peptide)


if __name__ == "__main__":
    main()
