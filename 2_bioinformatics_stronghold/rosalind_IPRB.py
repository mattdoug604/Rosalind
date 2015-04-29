#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Mendel's First Law
URL: http://rosalind.info/problems/iprb/

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
'''

def main():
    ''' Calculate the four different cases that
        would NOT result in an offspring with a
        dominant allele, then subtract that from
        1 to get the probability of an offspring
        that does.

        Dataset contains three integers, in order,
        corresponding to the number of homozygous
        dominant, heterozygous, and homozygous
        recessive individuals.
    '''
    with open('problem_datasets/rosalind_iprb.txt', 'r') as infile:
        k, m, n = map(float, infile.read().strip().split(' '))

    t = k + m + n
    
    c1 = k/t * (k-1)/(t-1) * 1/4
    c2 = k/t * n/(t-1) * 1/2
    c3 = n/t * k/(t-1) * 1/2
    c4 = n/t * (n-1)/(t-1)

    answer = 1 - (c1 + c2 + c3 + c4)
    print('%.5f' % answer)

if __name__ == '__main__': 
    main()
