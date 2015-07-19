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

    return(subtrees, level)

def distance_to_lca(subtrees, lca, node):
    binary = False
    
    # for each level in the tree...
    for i in range(lca, len(subtrees)):
        includes_node = False

        # for each node (and children) in that level...
        for sub in subtrees[i]:

            if ',' in sub:
                binary = True

            if node in sub:
                includes_node = True
                break

        if includes_node == False:
            if binary == True:
                dist = i - lca - 1
            else:
                dist = i - lca - 2
                
            return(dist)

    if binary == True:
        dist = len(subtrees) - lca - 1
    else:
        dist = len(subtrees) - lca - 2
        
    return(dist)
            

def find_distance(t):
    tree = t[0]
    a, b = t[1].split(' ')
    
    subtrees, lca = find_LCA(tree, a, b)
    dist = 2 + distance_to_lca(subtrees, lca, a) + distance_to_lca(subtrees, lca, b)
    
    return(dist)
    

def check_answer(ans_a, file):
    from rosalind_functions import check_nwck
    
    ''' Optional: check answers '''
    mismatches = []
    
    ans_b = check_nwck(file)
    for i in range(len(ans_a)):
        if ans_a[i] != ans_b[i]:
            mismatches.append(i)

    if len(mismatches) <= 0:
        print('no mismatches!\n', ' '.join(map(str, ans_a)), sep='')
    else:
        print('mismatches at: ',
              ' '.join(map(str, mismatches)), '\n',
              ' '.join(map(str, ans_a)),  '\n',
              ' '.join(map(str, ans_b)),  sep='')

def main():
    with open('problem_datasets/rosalind_nwck.txt' ,'r') as infile:
        trees = [l.split('\n') for l in infile.read().strip().split('\n\n')]

    answer = []
    for t in trees:
        answer.append(find_distance(t))

    #check_answer(answer, 'problem_datasets/rosalind_nwck.txt')
    print(' '.join(map(str, answer)))

if __name__ == '__main__':
    main()
