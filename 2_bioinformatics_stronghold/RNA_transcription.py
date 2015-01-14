#!/usr/bin/python
# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t.

dna = open("rosalind_rna.txt")
s = dna.read()
print s.replace("T", "U")
