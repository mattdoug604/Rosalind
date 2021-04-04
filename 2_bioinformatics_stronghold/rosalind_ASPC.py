#!/usr/bin/env python3

'''
Rosalind: Bioinformatics Stronghold
Problem: Introduction to Alternative Splicing
URL: http://rosalind.info/problems/aspc/

Given: Positive integers n and m with 0 <= m <= n <= 2000.
Return: The sum of combinations C(n,k) for all k satisfying m <= k <= n, modulo
1,000,000.
'''

'''
EXAMPLE INPUT:
6 3

EXAMPLE OUTPUT:
42
'''

from math import factorial as f

def combinations(n, m):
    return sum(f(n) // (f(k) * f(n-k)) for k in range(m, n+1))


def main():
    with open('problem_datasets/rosalind_aspc.txt', 'r') as infile:
        n, m = [int(i) for i in infile.readline().strip().split(' ')]

    answer = combinations(n, m) % 1000000
    print(answer)


if __name__ == '__main__':
    main()
