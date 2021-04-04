#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: The Wright-Fisher Model of Genetic Drift
URL: http://rosalind.info/problems/wfmd/

Given: Positive integers N (N≤7), m (m≤2N), g (g≤6) and k (k≤2N).

Return: The probability that in a population of N diploid individuals 
initially possessing m copies of a dominant allele, we will observe after g 
generations at least k copies of a recessive allele. Assume the Wright-Fisher 
model.
"""

from math import factorial as f


def probability(n, m, g, k):
    # Population is diploid so number of alleles is 2N
    n = 2 * n

    # Hold the frequency of each number of dominant alleles in the current pop.
    curr_gen = [0 for i in range(n + 1)]
    curr_gen[m] = 1

    # For each generation...
    for gen in range(g):
        next_gen = [0 for i in range(n + 1)]

        for i in range(n + 1):  # next generation...
            for j in range(n + 1):  # current geneneration...
                a = f(n) / f(i) / f(n - i)
                b = (j / n) ** i * (1 - (j / n)) ** (n - i)
                c = curr_gen[j]
                next_gen[i] += a * b * c

        curr_gen = next_gen

    return sum(curr_gen[:-k])


def main():
    # Read the input value.
    with open("problem_datasets/rosalind_wfmd.txt", "r") as infile:
        n, m, g, k = [int(i) for i in infile.read().strip().split(" ")]

    # Calculate and print the answer.
    print(probability(n, m, g, k))


if __name__ == "__main__":
    main()
