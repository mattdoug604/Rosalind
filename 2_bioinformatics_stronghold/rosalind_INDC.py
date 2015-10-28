#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Independent Segregation of Chromosomes
URL: http://rosalind.info/problems/indc/

Given: A positive integer n<=50.

Return: An array A of length 2n in which A[k] represents the common logarithm 
of the probability that two diploid siblings share at least k of their 2n 
chromosomes (we do not consider recombination for now).
'''

from math import factorial as f
from math import log10

def binomial_random_variable(n, k, p):
    a = f(n) / (f(k) * f(n-k))  # binomial coefficient
    b = (p**k) * ((1-p)**(n-k))
    c = a * b
    
    return c


def main():
    # Read the input value.
    with open('problem_datasets/rosalind_indc.txt', 'r') as infile:
        n = int(infile.read())
    
    # A distribution showing the probability of sharing exactly k chromosomes.
    prob = [binomial_random_variable(n*2, k, 0.5) for k in range(2*n, -1, -1)]
    
    # A list of the common logarithm of the probabilities of sharing 
    # *at least* k of n chromosomes.
    prob = [log10(sum(prob[:i])) for i in range(2*n, 0, -1)]
    
    # Output the answer.
    with open('output/rosalind_indc_out.txt', 'w') as outfile:
        outfile.write(' '.join(['%.3f' % i for i in prob]))
    

if __name__ == '__main__':
    main()
