#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Calculating Expected Offspring
URL: http://rosalind.info/problems/iev/

Given: Six positive integers, each of which does not exceed 20,000. The integers
correspond to the number of couples in a population possessing each genotype
pairing for a given factor. In order, the six given integers represent the
number of couples having the following genotypes:

1. AA-AA
2. AA-Aa
3. AA-aa
4. Aa-Aa
5. Aa-aa
6. aa-aa

Return: The expected number of offspring displaying the dominant phenotype in
the next generation, under the assumption that every couple has exactly two
offspring.
"""


def expected(f):
    return (f[0] * 1 + f[1] * 1 + f[2] * 1 + f[3] * 3 / 4 + f[4] * 1 / 2 + f[5] * 0) * 2


def main():
    with open("problem_datasets/rosalind_iev.txt", "r") as infile:
        f = [float(i) for i in infile.read().split()]

    answer = expected(f)
    print("%.1f" % answer)


if __name__ == "__main__":
    main()
