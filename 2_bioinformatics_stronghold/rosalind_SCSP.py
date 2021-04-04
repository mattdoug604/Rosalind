#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Interleaving Two Motifs
URL: http://rosalind.info/problems/scsp/

Given: Two DNA strings s and t.
Return: A shortest common supersequence of s and t. If multiple solutions exist,
you may output any one.
 
EXAMPLE INPUT:
ATCTGAT
TGCATA

EXAMPLE OUTPUT:
ATGCATGAT
"""

from rosalind_LCSQ import longest_sub


def shortest_sub(s, t):
    # Find the longest common subsequence.
    lcs = longest_sub(s, t)

    # Fill out the subsequence with the remaining char.
    scs = [""] * (len(lcs) + 1)

    m = 0
    n = 0
    for i in range(len(lcs)):
        # Increment through each DNA string while the character at position
        # m/n is not equal to the ith character of the longest subsequence,
        # appending the character(s) as you go.
        while s[m] != lcs[i] and m < len(s):
            scs[i] += s[m]
            m += 1
        while t[n] != lcs[i] and n < len(t):
            scs[i] += t[n]
            n += 1

        # Finally, add the ith character from the longest common subsequence,
        # and increment each DNA sequence by 1.
        scs[i] += lcs[i]
        m += 1
        n += 1

    # Append the remaining characters (if any) to form the supersequence.
    scs[-1] = s[m:] + t[n:]

    return "".join(scs)


def main():
    with open("problem_datasets/rosalind_scsp.txt", "r") as infile:
        s, t = infile.read().strip().split("\n")

    seq = shortest_sub(s, t)

    with open("output/rosalind_scsp_out.txt", "w") as outfile:
        outfile.write(seq)

    print("shortest common supersequence =", seq)


if __name__ == "__main__":
    main()
