#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Finding a Motif in DNA
URL: http://rosalind.info/problems/subs/

Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.
"""
from os.path import dirname, join

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_subs.txt")


def main():
    with open(INPUT_FILE, "r") as infile:
        s, t = infile.read().strip().split("\n")

    pos = []
    for i in range(len(s)):
        if s.startswith(t, i):
            pos.append(i + 1)  # Rosalind example uses 1-based numbering

    print(" ".join(map(str, pos)))


if __name__ == "__main__":
    main()
