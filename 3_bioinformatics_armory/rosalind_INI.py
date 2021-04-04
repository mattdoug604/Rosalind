#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Armory
Problem: Introduction to the Bioinformatics Armory
URL: http://rosalind.info/problems/ini/

Given: A DNA string s of length at most 1000 bp.
Return: Four integers (separated by spaces) representing the respective number
of times that the symbols 'A', 'C', 'G', and 'T' occur in s. Note: You must
provide your answer in the format shown in the sample output below.
"""
from os.path import dirname, join

from Bio.Seq import Seq

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_ini.txt")


def main():
    # Read the input file.
    with open(INPUT_FILE, "r") as infile:
        seq = Seq(infile.readline())

    # Count the number of each nucleotide.
    counts = map(seq.count, ["A", "C", "G", "T"])

    # Optional: print the answer.
    print(" ".join(map(str, counts)))

    # Output the answer.
    with open("output/rosalind_ini_out.txt", "w") as outfile:
        outfile.write(" ".join(map(str, counts)))


if __name__ == "__main__":
    main()
