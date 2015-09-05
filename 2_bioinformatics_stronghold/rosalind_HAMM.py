#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Counting Point Mutations
URL: http://rosalind.info/problems/hamm/

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
'''

def hamm_dist(dna):
    hamm = 0

    for i in range(len(dna[0])):
        if dna[0][i] != dna[1][i]:
            hamm +=1

    return hamm

def main():
    with open('problem_datasets/rosalind_hamm.txt', 'r') as f:
        seqs = f.read().split('\n')

    print(hamm_dist(seqs))


if __name__ =='__main__':
    main()
