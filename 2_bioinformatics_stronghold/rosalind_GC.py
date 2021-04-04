#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Computing GC Content
URL: http://rosalind.info/problems/gc/

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the
GC-content of that string. Rosalind allows for a default error of 0.001 in all
decimal answers unless otherwise stated; please see the note on absolute error
below.
"""
from os.path import dirname, join

from utils import parse_fasta

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_gc.txt")


def compute_gc(fastas):
    max_gc = 0
    max_h = ""

    for header, seq in fastas.items():
        gc = float(((seq.count("G") + seq.count("C")) / len(seq) * 100))
        if gc > max_gc:
            max_gc = gc
            max_h = header

    return (max_h, max_gc)


def main():
    fastas = parse_fasta(INPUT_FILE, no_id=False)
    max_h, max_gc = compute_gc(fastas)

    print(max_h, "\n", f"{max_gc:.6f}", sep="")


if __name__ == "__main__":
    main()
