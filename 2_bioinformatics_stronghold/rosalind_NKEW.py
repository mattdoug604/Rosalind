#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Newick Format with Edge Weights
URL: http://rosalind.info/problems/nkew/

Given: A collection of n weighted trees (n <= 40) in Newick format, with each tree containing at most 200 nodes; each tree Tk is followed by a pair of nodes xk and yk in Tk.
Return: A collection of n numbers, for which the kth number represents the distance between xk and yk in Tk.
'''

'''
EXAMPLE INPUT:
(dog:42,cat:33);
cat dog

((dog:4,cat:3):74,robot:98,elephant:58);
dog elephant

EXAMPLE OUTPUT:
75 136
'''

def parse_dist_value(sub_string):
    dist = ''
    for i in range(len(sub_string)):
        if sub_string[i].isdigit():
            dist += sub_string[i]
        else:
            break

    return(int(dist))


def find_lca(t, a, b):
    '''  Find the lowest common ancestor of both nodes being compared. Returns a partially complete
        list (unless the LCA is the root of the tree) of each level of the tree that contains the LCA, and
        the level of the tree containing the LCA.
    '''
    level = 0
    pos = []
    subtrees = list()
    
    for i in range(len(t)):
        if t[i] == '(':
            level += 1
            pos.append(i)
        elif t[i] == ')':
            sub = t[pos[-1]+1:i]
            if i+2 < len(t):
                val = parse_dist_value(t[i+2:])
            else:
                val = 0
            del pos[-1]

            while len(subtrees) < level:
                subtrees.append([])
                
            subtrees[level-1].append(sub+'..'+str(val))
            level -= 1
            
            if a in sub and b in sub:
                return(subtrees, level)              

    return(subtrees, level)


def distance_to_lca(lca, node):
    ''' Returns the distance from a given node to the LCA. '''
    dist = 0

    for i in lca[0]:
        if node in i:
            dist += parse_dist_value(i[i.index(node)+len(node)+1:])

    for j in range(len(lca)-1, 0, -1):
        for branch in lca[j]:
            if node in branch:
                dist += int(branch.split('..')[1])
    
    return(dist)


def distance_between_nodes(t):
    ''' Finds the pairwise distance between two nodes in a rooted tree. '''
    tree = t[0]
    a, b = t[1].split(' ')
    
    subtrees, lvl = find_lca(tree, a, b)
    dist = distance_to_lca(subtrees[lvl:], a) + distance_to_lca(subtrees[lvl:], b)
    
    return(dist)
    

def main():
    with open('problem_datasets/rosalind_nkew.txt' ,'r') as infile:
        trees = [l.split('\n') for l in infile.read().strip().split('\n\n')]

    answer = []
    for t in trees:
        answer.append(distance_between_nodes(t))

    print(' '.join(map(str, answer)))


if __name__ == '__main__':
    main()
