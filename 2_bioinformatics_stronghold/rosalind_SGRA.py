#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Using the Spectrum Graph to Infer Peptides
URL: http://rosalind.info/problems/sgra/

Given: A list L (of length at most 100) containing positive real numbers.

Return: The longest protein string that matches the spectrum graph of L (if 
multiple solutions exist, you may output any one of them). Consult the
monoisotopic mass table.
"""

from utils import mass_to_aa


def build_peptide(l, peptide="", aa=0):
    """Given a dictionary of fragment masses, with the next highest fragment
    mass and an amino acid representing the gap between them, iterably build a
    peptide by starting with the smallest mass.
    """
    if aa == 0:
        aa = min(l)

    if aa not in l:
        return peptide
    else:
        for i in l[aa]:
            return build_peptide(l, peptide + i[0], i[1])


def peptide_from_spectrum(l):
    # Create a directed graph of each mass and their possible associated amino
    # acids.
    pairs = {}
    for i in range(len(l)):
        for j in range(i, len(l)):
            aa = mass_to_aa(l[j] - l[i])
            if aa:
                if l[i] in pairs:
                    pairs[l[i]].append((aa, l[j]))
                else:
                    pairs[l[i]] = [(aa, l[j])]

    # Iterably build the peptide starting from the smallest mass.
    peptide = build_peptide(pairs)

    # Return the completed peptide of length n.
    return peptide


def main():
    with open("problem_datasets/rosalind_sgra.txt", "r") as infile:
        l = list(map(float, infile.readlines()))

    print(peptide_from_spectrum(l))


if __name__ == "__main__":
    main()
