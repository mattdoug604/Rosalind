#!/usr/bin/env python3

# Find patterns forming clumps in a string.
# Given: A string Genome, and integers k, L, and t.
# Return: All distinct k-mers forming (L, t)-clumps in Genome.

from collections import defaultdict

# 'Pattern' and 'Genome' are seperated by a line break
with open('rosalind_1d.txt', 'r') as in_file:
        both = in_file.read().split('\n')
        genome = both[0].rstrip()
        vals = both[1].split(' ')
        k = int(vals[0])
        L = int(vals[1])
        t = int(vals[2])

# Split the genome into substrings of length, k, starting on intervals starting from 0 to k.
def count_mer(gen, k, t):
    
    substrings = list()
    mer_count = defaultdict(int)

    # genome can be split into k reading frames,
    # identify each k-mer in a given frame
    for i in range(k):  
        mer = gen[i:]
        substrings += [mer[i:i+k] for i in range(0, len(mer), k)]

    # count the number of occurances of each k-mer in the genome
    for s in substrings:
        mer_count[s] += 1

    # filter out k-mers occuring less than t times
    results = [key for key, value in mer_count.items() if value >= t]
    return results

# Use count_mer() on each interval of length L, return a list of all the k-mers
# that appear at least t times.
def find_clumps(gen, k, L, t):

    kmers = []

    # for each interval of length, L, identify clumps in that interval
    for j in range(len(gen)-L-1):
        clumps = count_mer(gen[j:j+L], k, t)
        for clump in clumps:
            kmers.append(clump)

    # remove duplicates in the list
    return list(set(kmers))

# Find clump
for clump in find_clumps(genome, k, L, t):
    print clump
