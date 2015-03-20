#!/usr/bin/python
# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t), i.e. the number of differing nucleotides.

file = open("rosalind_hamm.txt", "r")
dna = file.read().split('\n')
s = dna[0]
t = dna[1]
file.close()

h_dist = 0
for i in range(len(s)):
    if s[i] <> t[i]:
        h_dist +=1

print h_dist
