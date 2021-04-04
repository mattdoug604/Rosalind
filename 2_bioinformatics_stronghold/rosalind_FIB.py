#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Rabbits and Recurrence Relations
URL: http://rosalind.info/problems/fib/

Positive integers n <= 40 and k <= 5.
Return: The total number of rabbit pairs that will be present after n months if
we begin with 1 pair and in each generation, every pair of reproduction-age
rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
"""
from os.path import dirname, join

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_fib.txt")


def fib(n, k):
    if n <= 1:
        return 1
    else:
        return fib(n - 1, k) + fib(n - 2, k) * k


def main():
    with open(INPUT_FILE, "r") as f:
        n, k = [int(i) for i in f.read().strip().split(" ")]

    print(fib(n - 1, k))


if __name__ == "__main__":
    main()
