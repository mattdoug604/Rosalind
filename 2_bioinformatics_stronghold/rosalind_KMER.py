#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: k-Mer Composition
URL: http://rosalind.info/problems/kmer/

Given: A DNA string s in FASTA format (having length at most 100 kbp).
Return: The 4-mer composition of s.
"""
from itertools import product
from os.path import dirname, join

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_kmer.txt")


def count_mers(seq, k=4):
    """Generate a dictionary of all possible k-mers, then iterate throught the
    sequence counting each k-mer present.
    """
    mer_dict = {i: 0 for i in ["".join(j) for j in list(product("ACGT", repeat=k))]}

    for i in range(len(seq) - k + 1):
        mer_dict[seq[i : i + k]] += 1

    return mer_dict


def composition(seq):
    """Count, sort, and arrange k-mer counts into a readable array."""
    mer_dict = count_mers(seq)

    array = []
    for i in sorted(mer_dict):
        array.append(mer_dict[i])

    array = " ".join([str(i) for i in array])

    return array


def main():
    with open(INPUT_FILE, "r") as infile:
        seq = "".join(infile.readlines()[1:]).replace("\n", "")

    answer = composition(seq)
    print(answer)


if __name__ == "__main__":
    main()
