#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Completing a Tree
URL: http://rosalind.info/problems/tree/

Given: A positive integer n (n <= 1000) and an adjacency list corresponding to a graph on n nodes that contains no cycles.
Return: The minimum number of edges that can be added to the graph to produce a tree.
'''

def completeNodes(n, adj_list):
    ''' Taking an adjacency list and a known number of nodes, fill in the
        gaps (i.e. add the nodes currently without edges to the list).
    '''
    check_list = [x for x in range(1, n+1)]

    ''' "Check off" the nodes that are in the adjacency list. '''
    for a, b in adj_list.items():
        if a in check_list:
            check_list.remove(a)
        if b in check_list:
            check_list.remove(b)

    ''' Fill in the adjacency list with the remaining (missing) nodes. '''
    for i in check_list:
        adj_list[i] = None

    return(adj_list)

def main():
    adj = {}
    
    with open('problem_datasets/rosalind_tree.txt', 'r') as infile:
        n = int(infile.readline())
        for i in infile.readlines():
            a, b = map(int, i.strip().split(' '))
            adj[a] = b

    adj = completeNodes(n, adj)
    print(adj)

if __name__ == '__main__':
    main()
