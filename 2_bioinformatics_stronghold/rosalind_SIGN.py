#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Enumerating Oriented Gene Orderings 
URL: http://rosalind.info/problems/sign/

Given: A positive integer n <= 6.
Return: The total number of signed permutations of length n, followed by a list of all such permutations (you may list the signed permutations in any order).
'''

import itertools


def get_perms(n):
    nums = [i for i in range(1, n+1)]
    start_perms = list(itertools.permutations(nums, n))
    new_perms = list()

    for perm in start_perms:
        for i in range(n+1):

            neg_list = list(itertools.combinations(nums, i))

            for neg in neg_list:
                temp = list(perm)
                for pos in neg:
                    temp[pos-1] = -temp[pos-1]

                new_perms.append(temp)

    new_perms = [' '.join(map(str, x)) for x in new_perms]

    return(len(new_perms), new_perms)


def main(n):
    with open('problem_datasets/rosalind_sign.txt', 'r') as infile:
        n = int(infile.read().strip())

    count, perms = get_perms(n)

    with open('output/rosalind_sign_out.txt', 'w') as outfile:
        outfile.write(str(count) + '\n')
        print(count, 'signed permutations.')
        for p in perms:
            outfile.write(p + '\n')

  
if __name__ == '__main__':
    n = 5
    main(n)
