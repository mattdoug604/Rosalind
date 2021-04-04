#!/usr/bin/env python3

'''
Rosalind: Bioinformatics Stronghold
Problem: Inferring mRNA from Protein
URL: http://rosalind.info/problems/mrna/

Given: A protein string of length at most 1000 aa.
Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)
'''

'''
CODON TABLE:
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G
'''

def count_mRNA(seq):
    codons = {'I':3, 'L':6, 'V':4, 'F':2,
              'M':1, 'C':2, 'A':4, 'G':4, 
              'P':4, 'T':4, 'S':6, 'Y':2, 
              'W':1, 'Q':2, 'N':2, 'H':2, 
              'E':2, 'D':2, 'K':2, 'R':6,
              '*':3 }

    if seq[-1] != '*':
        seq += '*'
        
    count = 1
    for s in seq:
        count *= codons[s]

    return count


def main():
    with open('problem_datasets/rosalind_mrna.txt', 'r') as infile:
        seq = infile.read().strip()

    print(count_mRNA(seq) % 1000000)


if __name__ == '__main__':
    main()
