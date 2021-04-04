#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Perfect Matchings and RNA Secondary Structures
URL: http://rosalind.info/problems/pmch/

Given: An RNA string s of length at most 80 bp having the same number of
occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.
Return: The total possible number of perfect matchings of basepair edges in the
bonding graph of s.
"""
from math import factorial
from os.path import dirname, join

from utils import parse_fasta

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_pmch.txt")


def main():
    rna = parse_fasta(INPUT_FILE)

    perfect = factorial(rna.count("A")) * factorial(rna.count("C"))
    print(perfect)

    with open("output/rosalind_pmch_out.txt", "w") as outfile:
        outfile.write(str(perfect))


if __name__ == "__main__":
    main()
