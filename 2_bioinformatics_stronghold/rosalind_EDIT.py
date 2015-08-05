#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Edit Distance
URL: http://rosalind.info/problems/edit/

Given: Two protein strings s and t in FASTA format (each of length at most 1000 aa).
Return: The edit distance dE(s,t).
'''

'''
EXAMPLE INPUT:
>Rosalind_39
PLEASANTLY
>Rosalind_11
MEANLY

...translates to a matrix that holds the distances between all prefixes of the
1st string and all prefixes of the 2nd.

       M E A N L Y
  [ 0  1 2 3 4 5 6]
P [ 1  1 2 3 4 5 6]
L [ 2  2 2 3 4 4 5]
E [ 3  3 2 3 4 5 5]
A [ 4  4 3 2 3 4 5]
S [ 5  5 4 3 3 4 5]
A [ 6  6 5 4 4 4 5]
N [ 7  7 6 5 4 5 5]
T [ 8  8 7 6 5 5 6]
L [ 9  9 8 7 6 5 6]
Y [10 10 9 8 7 6 5]

EXAMPLE OUTPUT:
5
'''

from rosalind_utils import parseFasta

def print_matrix(matrix, s, t):
    ''' Optional: Write out the distance matrix. '''
    print('Writing table...')
    with open('output/rosalind_edit_out.txt', 'w') as f:
        header = '     ' + ' '.join(t)
        f.write(header)
        f.write('\n')
        for x, m in enumerate(matrix):
            if x > 0:
                line = s[x-1] +' [' + ' '.join(map(str, m)) + ']'
            else:
                line = '  [' + ' '.join(map(str, m)) + ']'
            f.write(line)
            f.write('\n')

    
def edit_dist(strings):
    ''' Takes two DNA strings, of lengths m and n, and returns the edit distance
        between them. This is accomplished by building a matrix, l, that holds
        the distances between all prefixes of the 1st string and all prefixes of
        the 2nd. The edit distance is then the value of l[m, n].
    '''
    s, t = (strings[0], strings[1])
    m, n = (len(s), len(t))
    l = [[0 for x in range(n+1)] for y in range(m+1)]

    for i in range(1, m+1):
        l[i][0] = i

    for j in range(1, n+1):
        l[0][j] = j
        
    for j in range(1, n+1):
        for i in range(1, m+1):
            if s[i-1] == t[j-1]:
                l[i][j] = l[i-1][j-1]
            else:
                l[i][j] = min(l[i-1][j] + 1,   #a deletion
                              l[i][j-1] + 1,   #an insertion
                              l[i-1][j-1] + 1) #a substitution 

    #print_matrix(l, s, t)
    return(l[m][n])


def main():
    strings = list(parseFasta('problem_datasets/rosalind_edit.txt').values())
    print(edit_dist(strings))
    

if __name__ == '__main__':
    main()
