#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Longest Increasing Subsequence
URL: http://rosalind.info/problems/lgis/

Given: A positive integer n <= 10000 followed by a permutation π of length n.
Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.
'''

''' I found this thread (http://stackoverflow.com/questions/4938833/find-longest-increasing-sequence?rq=1)
    extremely helpful in understanding how to solve this problem.
'''

def longest_seq(n, seq, op='>'):
    ''' Find the longest subsequence (longest increasing subsequence by default)
        or a given sequence.
    '''
    # contains the max length of sub seq. ending at array[i]
    q = [0] * n
    # contains predecessor of the sub seq. ending at array[i]
    p = [-1] * n

    for i in range(n):
        maxLen = 0
    
        for j in range(i):
            if op == '>':
                check = seq[i] > seq[j]
            elif op == '<':
                check = seq[i] < seq[j]
                
            if check == True :
                if q[j] > maxLen:
                    maxLen = q[j]
                    p[i] = j

        q[i] = maxLen + 1

    idx = q.index(max(q))
    ls = []
    while(idx != -1):
        ls.append(seq[idx])
        idx = p[idx]

    return ls[::-1]

def main():
    with open('problem_datasets/rosalind_lgis.txt', 'r') as infile:
        n = int(infile.readline())
        perm = list(map(int, infile.readline().split(' ')))

    with open('output/rosalind_lgis_out.txt', 'w') as outfile:
        lgis = ' '.join(map(str, longest_seq(n, perm, '>')))
        lgds = ' '.join(map(str, longest_seq(n, perm, '<')))
        outfile.write(lgis + '\n' + lgds)

if __name__ == '__main__':
    main()
