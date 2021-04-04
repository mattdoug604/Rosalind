#!/usr/bin/env python3

"""
Rosalind: Bioinformatics Stronghold
Problem: Counting Disease Carriers
URL: http://rosalind.info/problems/afrq/

Given: An array A for which A[k] represents the proportion of homozygous
recessive individuals for the k-th Mendelian factor in a diploid population.
Assume that the population is in genetic equilibrium for all factors.

Return: An array B having the same length as A in which B[k] represents the
probability that a randomly selected individual carries at least one copy of
the recessive allele for the k-th factor.
"""

from math import sqrt


def probability(i):
    # f(aa) = p**2
    # i = p**2
    # p = sqrt(i)
    p = sqrt(i)

    # 1 = f(AA) + f(Aa) + f(aa)
    # 1 = p**2 + 2pq + q**2
    # 1 = (p + q)**2
    # sqrt(1) = p + q
    # q = 1 - p
    q = 1 - p

    # P(Aa or aa) = 2pq + p**2
    prob = (2 * p * q) + i

    return prob


def main():
    # Read the list of frequencies.
    with open("problem_datasets/rosalind_afrq.txt", "r") as infile:
        a = [float(i) for i in infile.read().strip().split(" ")]

    # Calculate the probability for each one.
    prob = [probability(i) for i in a]

    # Output the answer.
    with open("output/rosalind_afrq_out.txt", "w") as outfile:
        outfile.write(" ".join(["%.3f" % i for i in prob]))


if __name__ == "__main__":
    main()
