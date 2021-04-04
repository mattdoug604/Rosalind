#!/usr/bin/env python3

'''
Rosalind: Bioinformatics Stronghold
Problem: Wright-Fisher's Expected Behavior
URL: http://rosalind.info/problems/ebin/

Given: A positive integer n (n≤1000000) followed by an array P of length m 
(m≤20) containing numbers between 0 and 1. Each element of P can be seen as 
representing a probability corresponding to an allele frequency.

Return: An array B of length m for which B[k] is the expected value of 
Bin(n,P[k]); in terms of Wright-Fisher, it represents the expected allele 
frequency of the next generation.
'''

def main():
    # Read the input values.
    with open('problem_datasets/rosalind_ebin.txt', 'r') as infile:
        n = int(infile.readline())
        p = [float(i) for i in infile.readline().split(' ')]
        
    # The expected value for the allele frequency k is N * k
    answer = [n*k for k in p]
    
    # Output
    with open('output/rosalind_ebin_out.txt', 'w') as outfile:
        outfile.write(' '.join(map(str, answer)))
    

if __name__ == '__main__':
    main()
