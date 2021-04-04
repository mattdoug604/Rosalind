#!/usr/bin/env python3

'''
Rosalind: Bioinformatics Stronghold
Problem: Creating a Distance Matrix
URL: http://rosalind.info/problems/pdst/

Given: A collection of n (n <= 10) DNA strings s1,…,sn of equal length (at most
1 kbp). Strings are given in FASTA format.
Return: The matrix D corresponding to the p-distance dp on the given strings. As
always, note that your answer is allowed an absolute error of 0.001.
'''

'''
EXAMPLE INPUT:
>Rosalind_9499
TTTCCATTTA
>Rosalind_0942
GATTCATTTC
>Rosalind_6568
TTTCCATTTT
>Rosalind_1833
GTTCCATTTA

EXAMPLE OUTPUT:
0.00000 0.40000 0.10000 0.10000
0.40000 0.00000 0.40000 0.30000
0.10000 0.40000 0.00000 0.20000
0.10000 0.30000 0.20000 0.00000
'''

from rosalind_utils import parse_fasta

def calc_distance(s1, s2):
    dist = sum(1 if s1[i] != s2[i] else 0 for i in range(len(s1))) / len(s1)

    return dist


def distance_matrix(strings):
    matrix = [[0 for i in range(len(strings))] for j in range(len(strings))]

    for x in range(len(strings)):
        for y in range(len(strings)):
            dist = float("{0:.5f}".format(calc_distance(strings[x], strings[y])))
            matrix[x][y] = dist
            
    return matrix


def main():
    strings = parse_fasta('problem_datasets/rosalind_pdst.txt')
    matrix = distance_matrix(strings)

    with open('output/rosalind_pdst_out.txt', 'w') as outfile:
        for line in matrix:
            outfile.write(' '.join(map(str, line))+'\n')
    

if __name__ == '__main__':
    main()
