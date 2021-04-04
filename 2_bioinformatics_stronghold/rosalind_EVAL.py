#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Expected Number of Restriction Sites
URL: http://rosalind.info/problems/eval/

Given: A positive integer n (n <= 1,000,000), a DNA string s of even length at
most 10, and an array A of length at most 20, containing numbers between 0 and
1.

Return: An array B having the same length as A in which B[i] represents the
expected number of times that s will appear as a substring of a random DNA
string t of length n, where t is formed with GC-content A[i]
(see “Introduction to Random Strings”).

EXAMPLE INPUT:
10
AG
0.25 0.5 0.75

EXAMPLE OUTPUT:
0.422 0.563 0.422
"""


def gc_p(seq, gc):
    percent = 1
    prob_gc = gc / 2
    prob_at = (1 - gc) / 2

    for j in range(len(seq)):
        nt = seq[j]
        if nt == "G" or nt == "C":
            percent = percent * prob_gc
        elif nt == "A" or nt == "T":
            percent = percent * prob_at

    return percent


def prob(n, s, a):
    for i in a:
        prob = gc_p(s, i) * (n - 1)
        yield (prob)


def main():
    with open("problem_datasets/rosalind_eval.txt", "r") as infile:
        n, s, a = infile.read().strip().split("\n")
        n = int(n)
        a = [float(i) for i in a.split(" ")]

    print(" ".join([f"{p:.3f}" for p in prob(n, s, a)]))


if __name__ == "__main__":
    main()
