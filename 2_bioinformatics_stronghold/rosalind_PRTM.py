#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Calculating Protein Mass
URL: http://rosalind.info/problems/prtm/

Given: A protein string P of length at most 1000 aa.
Return: The total weight of P. Consult the monoisotopic mass table.
"""
from os.path import dirname, join

from utils import aa_mass

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_prtm.txt")


def calc_mass(prot):
    mass = 0

    for aa in prot:
        mass += aa_mass(aa)

    return mass


def main():
    with open(INPUT_FILE, "r") as infile:
        prot = "".join(infile.read().strip())

    answer = calc_mass(prot)
    print(f"{answer:.3f}")


if __name__ == "__main__":
    main()
