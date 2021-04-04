#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Calculating Protein Mass
URL: http://rosalind.info/problems/prtm/

Given: A protein string P of length at most 1000 aa.
Return: The total weight of P. Consult the monoisotopic mass table.
"""

from rosalind_utils import aa_mass


def calc_mass(prot):
    mass = 0

    for aa in prot:
        mass += aa_mass(aa)

    return mass


def main():
    with open("problem_datasets/rosalind_prtm.txt", "r") as infile:
        prot = "".join(infile.read().strip())

    answer = calc_mass(prot)
    print("%.3f" % answer)


if __name__ == "__main__":
    main()
