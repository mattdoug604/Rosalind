#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Matching Random Motifs
URL: http://rosalind.info/problems/rstr/

Given: A positive integer N <= 100000, a number x between 0 and 1, and a DNA
string s of length at most 10 bp.

Return: The probability that if N random DNA strings having the same length as
s are constructed with GC-content x (see “Introduction to Random Strings”), then
at least one of the strings equals s. We allow for the same random string to be
created more than once.
 
EXAMPLE INPUT:
90000 0.6
ATAGCCGA

EXAMPLE OUTPUT:
0.689
"""


def prob(n, gc, seq):
    percent = 1
    prob_gc = gc / 2
    prob_at = (1 - gc) / 2

    for i in seq:
        if i == "G" or i == "C":
            percent *= prob_gc
        elif i == "A" or i == "T":
            percent *= prob_at

    percent = 1 - (1 - percent) ** n

    return percent


def main():
    with open("problem_datasets/rosalind_rstr.txt", "r") as infile:
        n, s = infile.read().strip().split("\n")
        n, x = n.split(" ")
        n = int(n)
        x = float(x)

    print(f"{prob(n, x, s):.3}")


if __name__ == "__main__":
    main()
