#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Introduction to Set Operations
URL: http://rosalind.info/problems/seto/

Given: A positive integer n (n≤20,000) and two subsets A and B of {1,2,…,n}.

Return: Six sets: A∪B, A∩B, A−B, B−A, Ac, and Bc (where set complements are 
taken with respect to {1,2,…,n}).
"""
from os.path import dirname, join

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_seto.txt")


def main():
    with open(INPUT_FILE, "r") as infile:
        n = int(infile.readline().strip())
        a = set(map(int, infile.readline().strip()[1:-1].split(", ")))
        b = set(map(int, infile.readline().strip()[1:-1].split(", ")))

    with open("output/rosalind_seto_out.txt", "w") as outfile:
        answer = (
            set.union(a, b),
            set.intersection(a, b),
            set.difference(a, b),
            set.difference(b, a),
            set.difference(set(range(1, n + 1)), a),
            set.difference(set(range(1, n + 1)), b),
        )
        outfile.write("\n".join(map(str, answer)))


if __name__ == "__main__":
    main()
