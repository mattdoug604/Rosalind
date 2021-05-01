#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: The Founder Effect and Genetic Drift
URL: http://rosalind.info/problems/found/

Given: Two positive integers N and m, followed by an array A containing k 
integers between 0 and 2N. A[j] represents the number of recessive alleles for 
the j-th factor in a population of N diploid individuals.

Return: An m×k matrix B for which Bi,j represents the common logarithm of the 
probability that after i generations, no copies of the recessive allele for 
the j-th factor will remain in the population. Apply the Wright-Fisher model.
"""
from math import factorial as f
from math import log10
from os.path import dirname, join

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_foun.txt")


def fixation_prob(n, m, a):
    matrix = [[0 for i in range(len(a))] for j in range(m)]

    # Population is diploid so number of alleles is 2N
    n = 2 * n

    for i in range(len(a)):
        # Frequency of each number of recessive alleles in the current pop.
        curr_gen = [0 for x in range(n + 1)]
        curr_gen[a[i]] = 1

        # For each generatjon...
        for gen in range(m):
            next_gen = [0 for x in range(n + 1)]

            for j in range(n + 1):  # frequency in next generation...
                for k in range(n + 1):  # frequency in current geneneration...
                    p1 = f(n) / f(j) / f(n - j)
                    p2 = (k / n) ** j * (1 - (k / n)) ** (n - j)
                    p3 = curr_gen[k]
                    next_gen[j] += p1 * p2 * p3

            curr_gen = next_gen

            # Store the common logarithm of the answer.
            matrix[gen][i] = log10(curr_gen[0])

    return matrix


def main():
    # Read the input value.
    with open(INPUT_FILE, "r") as infile:
        n, m = map(int, infile.readline().strip().split(" "))
        a = list(map(int, infile.readline().strip().split(" ")))

    # Output the answer in matrix format.
    print(*line, sep=" ")


if __name__ == "__main__":
    main()s
