#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Complementing a Strand of DNA
URL: http://rosalind.info/problems/revc/

Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s.
'''

def main():
    with open('problem_datasets/rosalind_revc.txt', 'r') as infile:
        seq = infile.read().strip()

    seq_dict = { 'A':'T', 'T':'A', 'G':'C', 'C':'G' }
    revc = ''.join([seq_dict[base] for base in reversed(seq)])

    with open('output/rosalind_revc_out.txt', 'w') as outfile:
        print(revc)
        outfile.write(revc)

if __name__ == '__main__':
    main()
