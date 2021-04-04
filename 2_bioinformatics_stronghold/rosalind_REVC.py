#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Complementing a Strand of DNA
URL: http://rosalind.info/problems/revc/

Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s.
"""
from os.path import dirname, join

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_revc.txt")


def rev_comp(seq):
    seq_dict = {"A": "T", "T": "A", "G": "C", "C": "G"}
    revc = "".join([seq_dict[base] for base in reversed(seq)])

    return revc


def main():
    with open(INPUT_FILE, "r") as infile:
        seq = "".join(infile.read().strip())

    answer = rev_comp(seq)

    with open("output/rosalind_revc_out.txt", "w") as outfile:
        outfile.write(answer)


if __name__ == "__main__":
    main()
