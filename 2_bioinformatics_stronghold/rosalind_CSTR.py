#!/usr/bin/env python3

"""
Rosalind: Bioinformatics Stronghold
Problem: Creating a Character Table from Genetic Strings
URL: http://rosalind.info/problems/cstr/

Given: A collection of at most 100 characterizable DNA strings, each of length 
at most 300 bp.

Return: A character table for which each nontrivial character encodes the 
symbol choice at a single position of the strings. (Note: the choice of 
assigning '1' and '0' to the two states of each SNP in the strings is 
arbitrary.)
"""


def character_table(t):
    # Return if at the end of the sequence...
    if len(t[0]) < 1:
        return None

    # Can't create seperate taxa with only one sequence...
    if len(t) < 2:
        return None

    # Initialize the character table.
    char = [[0 for i in t]]

    taxa = [[0], []]
    for i in range(1, len(t)):
        if t[i][0] == t[0][0]:
            taxa[0].append(i)
        else:
            taxa[1].append(i)

    # Return if all sequences are identical at the current position...
    if taxa[1] == []:
        return None

    a, b = [[], []]
    for i in taxa[0]:
        char[0][i] = 1
        a.append(t[i][1:])
    for j in taxa[1]:
        b.append(t[j][1:])

    row1 = character_table(a)
    if row1 != None:
        for i in row1:
            char.append(i)

    row2 = character_table(b)
    if row2 != None:
        for j in row2:
            char.append(j)

    return char


def main():
    with open("problem_datasets/rosalind_cstr.txt", "r") as infile:
        strings = infile.read().strip().split("\n")

    answer = character_table(strings)

    print("\n".join(["".join(map(str, answer[i])) for i in range(len(answer))]))

    # with open('output/rosalind_ctbl_out.txt', 'w') as outfile:
    #    outfile.write('\n'.join([''.join(map(str, answer[i])) for i in range(len(answer))]))


if __name__ == "__main__":
    main()
