#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Introduction to Set Operations
URL: http://rosalind.info/problems/seto/

Given: A positive integer n (n≤20,000) and two subsets A and B of {1,2,…,n}.

Return: Six sets: A∪B, A∩B, A−B, B−A, Ac, and Bc (where set complements are 
taken with respect to {1,2,…,n}).
'''

def set_union(a, b):
    return '{' + ', '.join(map(str, set(a + b)))  + '}'
    
    
def set_intersect(a, b):
    return '{' + ', '.join(map(str, [i for i in a if i in b])) + '}'
    

def set_difference(a, b):
    return '{' + ', '.join(map(str, [i for i in a if i not in b])) + '}'
    
    
def main():
    with open('problem_datasets/rosalind_seto.txt', 'r') as infile:
        n = int(infile.readline().strip())
        a, b = [list(map(int, i[1:-1].split(', '))) for i in infile.read().strip().split('\n')]
    
    with open('output/rosalind_seto_out.txt', 'w') as outfile:
        outfile.write('\n'. join((set_union(a, b), 
                                  set_intersect(a, b), 
                                  set_difference(a, b), 
                                  set_difference(b, a), 
                                  set_difference(range(1, n+1), a), 
                                  set_difference(range(1, n+1), b))))
    

if __name__ == '__main__':
    main()