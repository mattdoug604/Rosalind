#!/usr/bin/env python3

# Find the most frequent k-mers in a string.
# Given: A DNA string 'Text' and an integer 'k'.
# Return: All most frequent k-mers in 'Text' (in any order).

from collections import defaultdict

text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4

# Split the genome into substrings of length, k, starting on intervals starting from 0 to k.
def count_mer(g, k):

    substrings = list()
    results = defaultdict(int)

    for i in range(k):
        mer = g[i:]
        substrings += [mer[i : i + k] for i in range(0, len(mer), k)]

    for s in substrings:
        results[s] += 1

    return results


# Find the max number of occurances and the corresponding k-mer(s)
kmers = count_mer(text, k)
max_count = max(kmers.values())
answer = [key for key, val in kmers.items() if val == max_count]
for a in answer:
    print(a)
