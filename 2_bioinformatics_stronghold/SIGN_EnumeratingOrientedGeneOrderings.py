#!/usr/bin/python
# SIGN_EnumeratingOrientedGeneOrderings.py

'''
Given: A positive integer n <= 6.
Return: The total number of signed permutations of length n, followed by a list of all such permutations (you may list the signed permutations in any order).
'''

import itertools

def getPerms(n):
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
    count, perms = getPerms(n)

    with open('rosalind_sign_out.txt', 'w') as outfile:
        outfile.write(str(count))
        outfile.write('\n')
        for p in perms:
            outfile.write(p)
            outfile.write('\n')
    
if __name__ == '__main__':
    n = 5
    main(n)
