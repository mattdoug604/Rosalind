#!/usr/bin/python

# Find patterns forming clumps in a string.
# Given: A string Genome, and integers k, L, and t.
# Return: All distinct k-mers forming (L, t)-clumps in Genome.

Genome = 'CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC'
k = 5 # length of k-mer to look for
L = 75 # length of interval on the genome to search
T = 4  # minimum amount of time the k-mer appears on the interval, L

# Make a dictionary of all k-mers and the number of occurances of each
kmers = {}
for i in range(len(Genome)-L+1):
        print (Genome[x:x+L])
