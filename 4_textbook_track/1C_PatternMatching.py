#!/usr/bin/env python3
"""
Find all occurrences of a pattern in a string.
Given: Strings 'Pattern' and 'Genome'.
Return: All starting positions in 'Genome' where 'Pattern' appears as a substring. Use 0-based indexing.
"""

import re

# 'Pattern' and 'Genome' are seperated by a line break
with open("problem_datasets/rosalind_1c.txt", "r") as in_file:
    both = in_file.read().split("\n")
    Pattern = both[0]
    Genome = both[1]

# Get the position of each match using a list comprehension
positions = [nt.start() for nt in re.finditer("(?=" + Pattern + ")", Genome)]

# Print out as a space-seperated string for readability
print(" ".join(map(str, positions)))
