#!/usr/bin/env python3

"""
Rosalind: Bioinformatics Stronghold
Problem: Transitions and Transversions
URL: http://rosalind.info/problems/tran/

Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
Return: The transition/transversion ratio R(s1,s2).
"""

from rosalind_utils import parse_fasta


def pointMutations(s1, s2):
    transitions = 0
    transversions = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if s1[i] == "A" and s2[i] == "G":
                transitions += 1
            elif s1[i] == "G" and s2[i] == "A":
                transitions += 1
            elif s1[i] == "C" and s2[i] == "T":
                transitions += 1
            elif s1[i] == "T" and s2[i] == "C":
                transitions += 1
            else:
                transversions += 1

    if transversions != 0:
        return transitions / transversions


def main():
    s1, s2 = parse_fasta("problem_datasets/rosalind_tran.txt")

    print(pointMutations(s1, s2))


if __name__ == "__main__":
    main()
