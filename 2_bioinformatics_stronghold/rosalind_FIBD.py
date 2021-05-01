#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Mortal Fibonacci Rabbits
URL: http://rosalind.info/problems/fibd/

Given: Positive integers n <= 100 and m <= 20.
Return: The total number of pairs of rabbits that will remain after the n-th
month if all rabbits live for m months.
"""
from os.path import dirname, join

INPUT_FILE = join(dirname(__file__), "problem_datasets", "rosalind_fibd.txt")


def rabbits(months, life):
    # Start with one baby rabbit.
    rabbits = [0 if i > 0 else 1 for i in range(life)]

    for i in range(months - 1):
        new_rabbits = [sum(rabbits[1:]) if x == 0 else 0 for x in range(life)]

        for j in range(len(rabbits)):
            if j < len(rabbits) - 1:
                new_rabbits[j + 1] = rabbits[j]  # rabbits aging
            else:
                rabbits[j] = 0  # kill off old rabbits

        rabbits = new_rabbits

    return sum(rabbits)


def main():
    with open(INPUT_FILE, "r") as infile:
        n, m = [int(i) for i in infile.read().strip().split(" ")]

    print(answer)


if __name__ == "__main__":
    main()
