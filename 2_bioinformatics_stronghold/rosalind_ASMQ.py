#!/usr/bin/env python3

"""
Rosalind: Bioinformatics Stronghold
Problem: Assessing Assembly Quality with N50 and N75
URL: http://rosalind.info/problems/asmq/

Given: A collection of at most 1000 DNA strings (whose combined length does
not exceed 50 kbp).

Return: N50 and N75 for this collection of strings.
"""


def Nxx(lenlist, xx):
    # Take the mean of the two middle elements if there are an even number
    # of elements. Otherwise, take the middle element.
    n = 100 / (100 - xx)
    medianpos = int(len(lenlist) / n)
    print(medianpos)
    if len(lenlist) % 2 == 0:
        return lenlist[medianpos] + lenlist[medianpos - 1] / n
    else:
        return lenlist[medianpos]


def main():
    with open("problem_datasets/rosalind_asmq.txt", "r") as infile:
        dna = infile.read().strip().split("\n")

    # Create a list containing n copies of an integer, n, where n is the
    # length of each given string in a list.
    lenlist = []
    for i in dna:
        lenlist += [len(i)] * len(i)
    lenlist = sorted(lenlist)
    print(len(lenlist))

    print(Nxx(lenlist, 50), Nxx(lenlist, 75))


if __name__ == "__main__":
    main()
