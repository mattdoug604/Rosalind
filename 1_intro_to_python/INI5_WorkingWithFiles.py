#!/usr/bin/env python3
# Given: A file containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

filename="problem_datasets/rosalind_ini5.txt"
counter = 0

for line in open(filename, "r"):
    if counter % 2 == 1:
        print(line.strip()) #.strip() removes any trailing whitespace/newlines
    counter += 1
