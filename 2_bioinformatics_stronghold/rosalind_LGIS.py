#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Longest Increasing Subsequence
URL: http://rosalind.info/problems/lgis/

Given: A positive integer n <= 10000 followed by a permutation π of length n.
Return: A longest increasing subsequence of π, followed by a longest decreasing
subsequence of π.
"""
from os.path import dirname, join

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_lgis.txt")


def longest_seq(n, seq, op):
    """Find the longest subsequence (increasing or decreasing specified by 'op')
    of a given sequence of integers.
    """
    q = [0] * n  # contains the max length of sub seq. ending at array[i]
    p = [-1] * n  # contains predecessor of the sub seq. ending at array[i]

    for i in range(n):
        maxLen = 0

        for j in range(i):
            if op == ">":
                check = seq[i] > seq[j]
            elif op == "<":
                check = seq[i] < seq[j]

            if check == True:
                if q[j] > maxLen:
                    maxLen = q[j]
                    p[i] = j

        q[i] = maxLen + 1

    idx = q.index(max(q))
    ls = []
    while idx != -1:
        ls = [seq[idx]] + ls
        idx = p[idx]

    return ls


def main():
    with open(INPUT_FILE, "r") as infile:
        n = int(infile.readline())
        perm = [int(i) for i in infile.readline().split(" ")]

    lgis = " ".join(map(str, longest_seq(n, perm, ">")))
    lgds = " ".join(map(str, longest_seq(n, perm, "<")))
    print(lgis + "\n" + lgds)


if __name__ == "__main__":
    main()
