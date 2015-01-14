#!/usr/bin/python

# Find the reverse complement of a DNA string.
# Given: A DNA string 'Pattern'.
# Return: 'Complement', the reverse complement of 'Pattern'.

with open('rosalind_1b_1_dataset.txt', 'r') as in_file:
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

print Complement[::-1]
