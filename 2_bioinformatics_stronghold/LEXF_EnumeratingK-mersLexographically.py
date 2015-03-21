#!/usr/bin/python
# LEXF_EnumeratingK-mersLexographically.py

'''
Given: A collection of at most 10 symbols defining an ordered alphabet, and a
    positive integer n (n <= 10).
Return: All strings of length n that can be formed from the alphabet, ordered
    lexicographically.
'''

import itertools

def permutations_with_replacement(alpha, n):
    perms = list(itertools.permutations(alpha, n))
    perms = [''.join(x) for x in perms]

    dups = [y*z for z in range(1, n+1) for y in alpha]
    i = 0
    for d in dups:
        perms.insert(i, d)
        i += len(alpha)+1

    return(perms)
        

def main():
    with open('problem_datasets/rosalind_lexf.txt', 'r') as infile:
        text = infile.read().strip().split('\n')
        alpha = text[0].split(' ')
        #n = int(text[1])
        n = 3

    answer = permutations_with_replacement(alpha, n)
    for i in answer:
        print(i)

if __name__ == '__main__':
    main()
