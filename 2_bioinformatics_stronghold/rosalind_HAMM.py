#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Counting Point Mutations
URL: http://rosalind.info/problems/hamm/

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
"""
from os.path import dirname, join

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_hamm.txt")


def hamm_dist(dna):
    hamm = 0

    for i in range(len(dna[0])):
        if dna[0][i] != dna[1][i]:
            hamm += 1

    return hamm


def main():
    with open(INPUT_FILE, "r") as f:
        seqs = f.read().split("\n")

    print(hamm_dist(seqs))


if __name__ == "__main__":
    main()
