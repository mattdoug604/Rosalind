#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Inferring Protein from Spectrum
URL: http://rosalind.info/problems/spec/

Given: A list L of n (n≤100) positive real numbers.
Return: A protein string of length n−1 whose prefix spectrum is equal to L (if
multiple solutions exist, you may output any one of them). Consult the
monoisotopic mass table.
 
EXAMPLE INPUT:
3524.8542
3710.9335
3841.974
3970.0326
4057.0646

EXAMPLE OUTPUT:
WMQS
"""

from utils import mass_to_aa


def calc_protein(l):
    prot = ""
    for i in range(1, len(l)):
        prot += mass_to_aa(l[i] - l[i - 1])

    return prot


def main():
    # Read in the list of prefix weights.
    with open("problem_datasets/rosalind_spec.txt", "r") as infile:
        l = list(map(float, infile.read().strip().split("\n")))

    # Print answer.
    print(calc_protein(l))


if __name__ == "__main__":
    main()
