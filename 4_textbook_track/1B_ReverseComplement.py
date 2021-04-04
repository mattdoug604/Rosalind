#!/usr/bin/env python3

# Find the reverse complement of a DNA string.
# Given: A DNA string 'Pattern'.
# Return: 'Complement', the reverse complement of 'Pattern'.

with open('problem_datasets/rosalind_1b.txt', 'r') as in_file:
        Pattern = in_file.read()
        
Complement = ''
for nt in Pattern:
        if nt == 'A':
                Complement += 'T'
        elif nt == 'T':
                Complement += 'A'
        elif nt == 'C':
                Complement += 'G'
        elif nt == 'G':
                Complement += 'C'

print(Complement[::-1])
