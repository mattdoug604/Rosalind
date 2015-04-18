#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Counting Point Mutations
URL: http://rosalind.info/problems/hamm/

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
'''

def main():
    with open("problem_datasets/rosalind_hamm.txt", "r") as infile:
        dna = infile.read().split('\n')

    h_dist = 0
    for i in range(len(dna[0])):
        if dna[0][i] <> dna[1][i]:
            h_dist +=1

    print h_dist

if __name__ =='__main__':
    main()
