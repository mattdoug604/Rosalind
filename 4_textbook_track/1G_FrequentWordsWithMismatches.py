#!/usr/bin/env python3
"""
Find the most frequent k-mers with mismatches in a string.
Given: A string genome as well as integers k and d.
Return: All most frequent k-mers with up to d mismatches in genome.
"""
import itertools
from collections import defaultdict
from os.path import dirname, join

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_1g.txt")


# Split the genome into substrings of length, k, starting on intervals starting from 0 to k.
def count_mer(gen, k):
    kmer_list = ["".join(nt) for nt in itertools.product(["A", "T", "C", "G"], repeat=k)]
    kmers = list()
    mismatches = defaultdict(int)

    # genome can be split into k reading frames,
    # identify each k-mer in a given frame
    for i in range(k):
        frame = gen[i:]
        kmers += [frame[i : i + k] for i in range(0, len(frame), k) if len(frame[i : i + k]) >= k]

    # count the number of occurances of each k-mer in the genome
    for mer1 in kmer_list:
        for mer2 in kmers:
            diff = 0
            if mer1 != mer2:
                for nt in range(k):
                    if mer1[nt] != mer2[nt]:
                        diff += 1
            if diff <= d:
                mismatches[mer1] += 1

    return mismatches


# Read file
with open(INPUT_FILE, "r") as in_file:
    text = in_file.read().split("\n")
    genome = text[0]
    val = text[1].split(" ")
    k = int(val[0])
    d = int(val[1])

# Find the max number of occurances and the corresponding k-mer(s)
kmers = count_mer(genome, k)
max_count = max(kmers.values())
answer = [key for key, val in kmers.items() if val == max_count]
for a in answer:
    print(a)
