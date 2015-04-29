#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: k-Mer Composition
URL: http://rosalind.info/problems/kmer/

Given: A DNA string s in FASTA format (having length at most 100 kbp).
Return: The 4-mer composition of s.
'''

from itertools import product

def countMers(seq, k):
    ''' Generate a dictionary of all possible k-mers, then iterate throught the
        sequence counting each k-mer present.
    '''
    mer_dict = { i:0 for i in [''.join(j) for j in list(product('ACGT', repeat=k))] }
    
    for i in range(len(seq)-k+1):
        mer_dict[seq[i:i+k]] += 1

    return(mer_dict)

def composition(seq, k):
    ''' Count, sort, and arrange k-mer counts into a readable array. '''
    mer_dict = countMers(seq, k)

    array = []
    for i in sorted(mer_dict):
        array.append(mer_dict[i])

    array = ' '.join([str(i) for i in array])
    return(array)

def main():
    k = 4
    
    with open('problem_datasets/rosalind_kmer.txt', 'r') as infile:
        seq = ''.join(infile.readlines()[1:]).replace('\n', '')

    with open('output/rosalind_kmer_out.txt', 'w') as outfile:
        outfile.write(composition(seq, k))
    
if __name__ == '__main__':
    main()
