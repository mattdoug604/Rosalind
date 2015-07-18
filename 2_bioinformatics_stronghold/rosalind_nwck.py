#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Distances in Trees
URL: http://rosalind.info/problems/nwck/

Given: A collection of n trees (n <= 40) in Newick format, with each tree containing at most 200 nodes; each tree Tk is followed by a pair of nodes xk and yk in Tk.
Return: A collection of n positive integers, for which the kth integer represents the distance between xk and yk in Tk.
'''

def find_LCA(t, a, b):
    level = 0
    pos = []
    subtrees = []
    
    for i in range(len(t)):
        if t[i] == '(':
            level += 1
            pos.append(i)
        elif t[i] == ')':
            sub = t[pos[-1]+1:i]
            del pos[-1]

            while len(subtrees) < level:
                subtrees.append([])
                
            subtrees[level-1].append(sub)
            level -= 1
            
            #check if subtree contains both nodes
            if a in sub and b in sub:
                return(subtrees, level)
            

def find_distance(t):
    tree = t[0]
    #a, b = t[1].split(' ')
    a = 'a'
    b = 'b'
    print('find', a, '->', b)
    
    subtrees, lvl = find_LCA(tree, a, b)
    lca = subtrees[lvl]
    dist = len(subtrees) - (lvl+1)
    print(subtrees, lca, dist)
    

def main():
    with open('problem_datasets/rosalind_test2.txt' ,'r') as infile:
        trees = [l.split('\n') for l in infile.read().strip().split('\n\n')]

    answer = []
    answer.append(find_distance(trees[0]))
    
    #for t in trees:
    #    answer.append(find_distance(t))

    #print(' '.join(map(str, answer)))
    

if __name__ == '__main__':
    main()
