#!/usr/bin/python
# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement t of s.

dna = open("rosalind_revc.txt", "r")
s = dna.read()
t = []

for nt in list(s):
    if nt in "A":
        t.append("T")
    elif nt in "T":
        t.append("A")
    elif nt in "C":
        t.append("G")
    elif nt in "G":
        t.append("C")

t.reverse()
t = ''.join(t)
print t
