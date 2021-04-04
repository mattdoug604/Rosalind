#!/usr/bin/env python3
"""
Find the reverse complement of a DNA string.
Given: A DNA string 'Pattern'.
Return: 'Complement', the reverse complement of 'Pattern'.
"""
from os.path import dirname, join

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_1b.txt")


with open(INPUT_FILE, "r") as in_file:
    Pattern = in_file.read()

Complement = ""
for nt in Pattern:
    if nt == "A":
        Complement += "T"
    elif nt == "T":
        Complement += "A"
    elif nt == "C":
        Complement += "G"
    elif nt == "G":
        Complement += "C"

print(Complement[::-1])
