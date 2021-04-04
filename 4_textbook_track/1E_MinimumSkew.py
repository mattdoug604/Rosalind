#!/usr/bin/env python3
"""
Find a position in a genome minimizing the skew.
Given: A DNA string Genome.
Return: All integer(s) i minimizing Skew(Prefix,i (Text)) over all values of i (from 0 to |Genome|).

Example:
   C  A  T G G G C A T C G G C C A T A  C G  C  C
0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2
"""
from os.path import dirname, join

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_1e.txt")


def find_min_skew(genome):
    counts = {}
    skew = 0

    for i in range(len(genome)):
        if genome[i] == "C":
            skew -= 1
        elif genome[i] == "G":
            skew += 1

        counts[i + 1] = skew

    return counts


# Read file
with open(INPUT_FILE, "r") as in_file:
    genome = in_file.read().rstrip()

# Find the smallest skew value and associated value(s) of i
skews = find_min_skew(genome)
min_skew = min(skews.values())
answer = [key for key, val in skews.items() if val == min_skew]
for a in answer:
    print(a)
