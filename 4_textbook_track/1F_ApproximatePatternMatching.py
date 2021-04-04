#!/usr/bin/env python3

# Find all approximate occurrences of a pattern in a string.
# Given: Strings Pattern and Text along with an integer d.
# Return: All starting positions where Pattern appears as a substring of Text with at most d mismatches.

# Read file
with open("problem_datasets/rosalind_1f.txt", "r") as in_file:
    text = in_file.read().split("\n")
    pattern = text[0]
    genome = text[1]
    d = int(text[2])


def pattern_match(gen, pat, d):

    results = []

    for i in range(len(gen) - len(pat)):
        diff = 0
        string = gen[i : i + len(pat)]
        for j in range(len(string)):
            if string[j] != pat[j]:
                diff += 1

        if diff <= d:
            results.append(i)

    return results


for p in pattern_match(genome, pattern, d):
    print(p)
