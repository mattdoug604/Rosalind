#!/usr/bin/python
# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

dna = open("rosalind_dna.txt")
s = dna.read()
a = 0
c = 0
g = 0
t = 0

for nt in list(s):
    if "a" in nt.lower():
        a += 1
    elif "c" in nt.lower():
        c += 1
    elif "g" in nt.lower():
        g += 1
    elif "t" in nt.lower():
        t += 1

print a, c, g, t
