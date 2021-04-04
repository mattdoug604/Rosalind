#!/usr/bin/env python3

"""
Rosalind: Bioinformatics Stronghold
Problem: Introduction to Random Strings
URL: http://rosalind.info/problems/prob/

Given: A DNA string s of length at most 100 bp and an array A containing at 
most 20 numbers between 0 and 1.

Return: An array B having the same length as A in which B[k] represents the
common logarithm of the probability that a random string constructed with the
GC-content found in A[k] will match s exactly.
"""

from math import log10


def prob(seq, gc):
    p = []

    for i in range(len(gc)):
        percent = 1
        prob_gc = gc[i] / 2
        prob_at = (1 - gc[i]) / 2

        for j in range(len(seq)):
            nt = seq[j]
            if nt == "G" or nt == "C":
                percent *= prob_gc
            elif nt == "A" or nt == "T":
                percent *= prob_at

        percent = log10(percent)
        p.append(percent)

    return p


def main():
    with open("problem_datasets/rosalind_prob.txt", "r") as infile:
        seq, gc = infile.read().strip().split("\n")
        gc = [float(x) for x in gc.split(" ")]

    answer = prob(seq, gc)

    print(" ".join(["%.3f" % i for i in answer]))


if __name__ == "__main__":
    main()
