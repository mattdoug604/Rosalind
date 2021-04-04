#!/usr/bin/env python3

'''
Rosalind: Bioinformatics Stronghold
Problem: Reversal Distance
URL: http://rosalind.info/problems/rear/

Given: A collection of at most 5 pairs of permutations, all of which have length
10.
Return: The reversal distance between each permutation pair.
'''

'''
Input:
1 2 3 4 5 6 7 8 9 10
3 1 5 2 7 4 9 6 10 8

3 10 8 2 5 4 7 1 6 9
5 2 3 1 7 4 10 8 6 9

8 6 7 9 4 1 3 10 2 5
8 2 7 6 9 1 5 3 10 4

3 9 10 4 1 8 6 7 5 2
2 9 8 5 1 7 3 4 6 10

1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10

Output:
9 4 5 7 0
'''

def split_pair(pair):
    ''' Convert two permutations strings to two lists of integers. '''
    p1, p2 = [list(map(int, p.split(' '))) for p in pair]
    
    return p1, p2


def breakpoint(p):
    ''' Returns a list of elements in the given permutation where a breakpoint
        occurs.
    '''
    bp = []
    for i in range(1, len(p)):
        if abs(p[i] - p[i-1]) > 1:
            bp.append(i)
    
    return bp


def printRound(p, a, b):
    ''' Optional: format and print the current reversal. '''
    if 10 in p[a:b]:
        x = 1
    else:
        x = 2
        
    print(p, ' - ', '(', a, ',', b-1, ')', sep='')
    print(' ', ' '*(a*3), '-'*((b-a)*3-x), sep='')


def reversal_dist(p1, p2):
    ''' Determine the minimum reversal distance for a pair of permutations by
        performing a greedy search.
    '''

    ''' Perform a quick check to see if the pair is already the same. '''
    if p1 == p2:
        return(0)
    
    ''' Prepend 0 and append len(permutation)+1 to determine if endpoints are
        correct. '''
    p_start = [0] + [p1.index(x)+1 for x in p2] + [len(p1)+1]
    #print('-'*50, '\n', p_start, ' <-- reverse\n', sep='')

    ''' Set starting permutations as the best current permutation. '''
    perm_list = [p_start]
    bp_min = len(breakpoint(p_start))

    ''' The maximum required number of reversals to solve this is
        len(permutation) + 1, so loop until we hit that mark, or solve the
        problem.
    '''
    count = 0
    while count < len(p_start)+1:
        #print('Round #%i' % int(count+1))
        new_perms = []

        count += 1

        for perm in perm_list:
            bp = breakpoint(perm)

            ''' Reverse each pair of breakpoints '''
            for i in range(len(bp)):
                for j in range(i+1, len(bp)):
                    a = bp[i]
                    b = bp[j]
                    if b-a > 1:

                        p_new = perm[:a] + list(reversed(perm[a:b])) + perm[b:]
                        bp_new = len(breakpoint(p_new))

                        ''' Problem solved when no breakpoints remain. The
                            reversal(s) with the least breakpoints is/are the
                            best choice in this case, so we can throw out the
                            others.
                        '''
                        if bp_new == 0:
                            #print('breakpoints = %i' % bp_new)
                            #printRound(p_new, a, b)
                            return count
                        elif bp_new < bp_min:
                            #print('breakpoints = %i' % bp_new)
                            #printRound(p_new, a, b)
                            bp_min = bp_new
                            new_perms = [p_new]
                        elif bp_new == bp_min:
                            #printRound(p_new, a, b)
                            new_perms.append(p_new)

        perm_list = new_perms


def main():
    with open('problem_datasets/rosalind_rear.txt', 'r') as infile:
        permutations = [x.split('\n') for x in infile.read().strip().split('\n\n')]
        permutations = [split_pair(pair) for pair in permutations]

    counts = [min(reversal_dist(pair[0], pair[1]),
                  reversal_dist(pair[1], pair[0])) for pair in permutations]

    print(' '.join(map(str, counts)))


if __name__ == '__main__':
    main()
