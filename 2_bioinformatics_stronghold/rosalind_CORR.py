#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Error Correction in Reads
URL: http://rosalind.info/problems/corr/

Given: A collection of up to 1000 reads of equal length (at most 50 bp) in FASTA
format. Some of these reads were generated with a single-nucleotide error. For
each read s in the dataset, one of the following applies:

    - s was correctly sequenced and appears in the dataset at least twice
      (possibly as a reverse complement);
    - s is incorrect, it appears in the dataset exactly once, and its Hamming
      distance is 1 with respect to exactly one correct read in the dataset (or
      its reverse complement).

Return: A list of all corrections in the form "[old read]->[new read]". (Each
correction must be a single symbol substitution, and you may return the 
corrections in any order.)
'''

'''
EXAMPLE INPUT:
>Rosalind_52
TCATC
>Rosalind_44
TTCAT
>Rosalind_68
TCATC
>Rosalind_28
TGAAA
>Rosalind_95
GAGGA
>Rosalind_66
TTTCA
>Rosalind_33
ATCAA
>Rosalind_21
TTGAT
>Rosalind_18
TTTCC

EXAMPLE OUTPUT:
TTCAT->TTGAT
GAGGA->GATGA
TTTCC->TTTCA
'''

from rosalind_utils import parse_fasta
from rosalind_utils import reverse_complement as rev_comp

'''
def rev_comp(string):
    ''' '''Return the reverse complement of a given DNA string. ''''''
    rev = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    rev_string = ''.join([rev[i] for i in string[::-1]])

    return rev_string
'''

def hamm_dist(a, b, limit=1):
    ''' Calculate the Hamming distance of two DNA strings. For this problem we
        only care if the Hamming distance is greater than 1 or not.
    ''' 
    hamm = 0
    
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            hamm += 1
        if hamm > limit:
            return(hamm)

    return hamm

def count_apperances(string_list):
    ''' Count how many times a given DNA string occurs in a list. If the reverse
        complement of that string occurs in the list, it counts towards the
        original.
    '''
    str_count = {}

    for i in string_list:
        if i in str_count:
            str_count[i] += 1
        else:
            if rev_comp(i) in str_count:
                str_count[rev_comp(i)] += 1
            else:
                str_count[i] = 1
                str_count[rev_comp(i)] = 1

    return str_count


def error_correct(string_list):
    ''' Identify single symbol substitutions by comparing strings to a list of
        known correct strings (i.e. those that occur one or more times in the
        list).
    '''
    
    counts = count_apperances(string_list)
    correct = []
    incorrect = []
    corrections = []
    
    for j in counts:
        if counts[j] > 1:
            correct.append(j)
        else:
            incorrect.append(j)

    for i in incorrect:
        for j in correct:
            if hamm_dist(i, j) < 2:
                corrections.append([i, j])

    return corrections


def main():
    strings = parse_fasta('problem_datasets/rosalind_corr.txt')
    strings += [rev_comp(i) for i in strings]

    corr = error_correct(strings)
    
    with open('output/rosalind_corr_out.txt', 'w') as outfile:
        for i in corr:
            outfile.write('->'.join(i) + '\n')


if __name__ == '__main__':
    main()
