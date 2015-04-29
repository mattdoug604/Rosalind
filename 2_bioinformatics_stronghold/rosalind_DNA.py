#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Counting DNA Nucleotides
URL: http://rosalind.info/problems/dna/

Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
'''

def main():
    with open('problem_datasets/rosalind_dna.txt', 'r') as infile:
        dna = infile.read()

    counts = map(dna.count, ['A', 'C', 'G', 'T'])

    print(' '.join(map(str, counts)))

if __name__ == '__main__':
    main()
