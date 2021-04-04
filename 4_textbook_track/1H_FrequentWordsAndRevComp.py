#!/usr/bin/env python3

# Find the most frequent k-mers (with mismatches and reverse complements) in a DNA string.
# Given: A DNA string Text as well as integers k and d.
# Return: All k-mers Pattern maximizing the sum Count.d(Text, Pattern) + Count.d(Text, RevCompPattern) over all possible k-mers.

import itertools
from collections import defaultdict


def revCompSeq(seq):
    revSeq = seq[::-1]
    revComp = ""
    for nt in revSeq:
        if nt == "A":
            revComp += "T"
        elif nt == "T":
            revComp += "A"
        elif nt == "C":
            revComp += "G"
        elif nt == "G":
            revComp += "C"

    return revComp


# Split the genome into substrings of length, k, starting on intervals starting from 0 to k.
def defineMer(gen, k):
    dsDNA = [gen, revCompSeq(gen)]
    kmers = list()

    # genome can be split into k reading frames,
    # identify each k-mer in a given frame
    for strand in dsDNA:
        for i in range(k):
            frame = strand[i:]
            kmers += [
                frame[i : i + k] for i in range(0, len(frame), k) if len(frame[i : i + k]) >= k
            ]

    return kmers


# count the number of occurances of each k-mer in the genome
def countMer(gen, k):
    foundMers = defineMer(gen, k)
    kmerList = ["".join(nt) for nt in itertools.product(["A", "T", "C", "G"], repeat=k)]
    mismatches = defaultdict(int)

    for mer1 in kmerList:
        for mer2 in foundMers:
            diff = 0
            if mer1 != mer2:
                for nt in range(k):
                    if mer1[nt] != mer2[nt]:
                        diff += 1
            if diff <= d:
                mismatches[mer1] += 1

    return mismatches


# Read file
with open("problem_datasets/rosalind_1h.txt", "r") as in_file:
    text = in_file.read().split("\n")
    genome = text[0]
    val = text[1].split(" ")
    k = int(val[0])
    d = int(val[1])

# Find the max number of occurances and the corresponding k-mer(s)
kmers = countMer(genome, k)
max_count = max(kmers.values())
answer = [key for key, val in kmers.items() if val == max_count]
for a in answer:
    print(a)
