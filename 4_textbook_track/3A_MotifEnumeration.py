#!/usr/bin/env python3
"""
Find all (k, d)-motifs in a collection of strings.
Given: Integers k and d, followed by a collection of strings Dna.
Return: All (k, d)-motifs in Dna.

A motif only counts if it occurs in *all* dna strings!
Method: start with an arbitrary dna string, get a list of all kmers (with
mismatches) in that string, compare those to kmers (with mismatches) in the
next string, eliminate any kmers that do not appear in both strings. Continue
for the remaining strings.
"""

import itertools


def findMers(seqs, k, d):
    # Start with list of all possible k-mers
    motifs = ["".join(nt) for nt in itertools.product(["A", "C", "T", "G"], repeat=k)]

    # Get all k-mers present in each dna string
    for dna in seqs:
        kmers = []
        for i in range(len(dna) - k + 1):
            kmers.append(dna[i : i + k])

        # Find the interection between found k-mers, and k-mers present in
        # the previous string.
        newMotifs = [c for c in compMotifs(kmers, motifs, k, d)]
        motifs = list(set(motifs) and set(newMotifs))

    # Remaining k-mers are present in all dna strings.
    return motifs


def compMotifs(kmers, motifs, k, d):
    for mer1 in motifs:
        for mer2 in kmers:
            diff = 0
            for nt in range(k):
                if diff <= d:
                    if mer1[nt] != mer2[nt]:
                        diff += 1
                else:
                    break
            if diff <= d:
                yield (mer1)


with open("problem_datasets/rosalind_3a.txt", "r") as infile:
    text = infile.read().rstrip().split("\n")
    k = int(text[0].split(" ")[0])
    d = int(text[0].split(" ")[1])
    strings = text[1:]

answer = " ".join(findMers(strings, k, d))
print(answer)

# Input:
# 3 1
# ATTTGGC
# TGCCTTA
# CGGTATC
# GAAAATT
#
# Output:
# ATA ATT GTT TTT
