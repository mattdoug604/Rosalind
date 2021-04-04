#!/usr/bin/env python3

"""
Rosalind: Bioinformatics Stronghold
Problem: Matching a Spectrum to a Protein
URL: http://rosalind.info/problems/prsm/

Given: A positive integer nn followed by a collection of nn protein strings 
s1s1, s2s2, ..., snsn and a multiset RR of positive numbers (corresponding to 
the complete spectrum of some unknown protein string).

Return: The maximum multiplicity of R⊖S[sk] taken over all strings sk, 
followed by the string sk for which this maximum multiplicity occurs (you may 
output any such value if multiple solutions exist).
"""

from decimal import *

from rosalind_utils import aa_mass

getcontext().prec = 8


def possible_masses(p):
    # Calculate the masses of all possible fragments from a given peptide.
    masses = []

    for i in range(len(p)):
        masses.append(Decimal(aa_mass(p[:i])))
        masses.append(Decimal(aa_mass(p[i:])))

    return masses


def multiplicity(s, t):
    # Calculate the most common Minkowski difference from both sets.
    sets = {}

    for i in s:
        for j in t:
            d = i - j
            if d in sets:
                sets[d] += 1
            else:
                sets[d] = 1

    # Find the largest multiplicity and return it.
    largest = max((v, k) for k, v in sets.items())

    return largest


def main():
    # Vairables to hold the largest multiplicity and associated peptide.
    most_occurances = 0
    most_peptide = ""

    # Read the integer, n, the peptides, and the complete spectrum.
    with open("problem_datasets/rosalind_prsm.txt", "r") as infile:
        n = int(infile.readline())
        peptides = [infile.readline().strip() for i in range(n)]
        spectrum = [Decimal(i) for i in infile.readlines()]

    # Comapre each peptide to the given spectrum
    for i in peptides:
        occurances, k = multiplicity(possible_masses(i), spectrum)

        if occurances >= most_occurances:
            most_occurances = occurances
            most_peptide = i

    # Print the answer.
    print(most_occurances, "\n", most_peptide, sep="")


if __name__ == "__main__":
    main()
