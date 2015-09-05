#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Independent Alleles
URL: http://rosalind.info/problems/lia/

Given: Two positive integers k (k <= 7) and N (N <= 2k). In this problem, we
begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two
children in the 1st generation, each of whom has two children, and so on. Each
organism always mates with an organism having genotype Aa Bb.
Return: The probability that at least N Aa Bb organisms will belong to the k-th
generation of Tom's family tree (don't count the Aa Bb mates at each level).
Assume that Mendel's second law holds for the factors.
'''

def binomial(k, n):
    if k > n - k:
        k = n - k

    total = 1
    for i in range(1, k + 1):
        total *= (n - (k - i))
        total /= i

    return total


def prob(k, n):
    return binomial(n, 2**k) * 0.25**n * 0.75**(2**k - n)


def getProb(k, n):
    ''' The probability that N AaBb organisms belong to the k-th generation is
        1 minus the sum of the probability that they don't.
    '''
    return 1 - sum(prob(k, i) for i in range(n))


def main():
    ''' Read a text file containing two integers, k and n, respectively.
        Rosalind give the answer to three decimal places.
    '''
    with open('problem_datasets/rosalind_lia.txt', 'r') as infile:
        k, n = map(int, infile.read().strip().split(' '))

    print('%.3f' % getProb(k, n))


if __name__ == '__main__':
    main()
