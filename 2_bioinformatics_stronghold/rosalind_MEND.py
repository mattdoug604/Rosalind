#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Inferring Genotype from a Pedigree
URL: http://rosalind.info/problems/mend/

Given: A rooted binary tree T in Newick format encoding an individual's 
pedigree for a Mendelian factor whose alleles are A (dominant) and a 
recessive).

Return: Three numbers between 0 and 1, corresponding to the respective 
probabilities that the individual at the root of T will exhibit the "AA", "Aa" 
and "aa" genotypes.
'''

def subtrees(t):
    ''' Split a Newick formatted tree into seperate subtrees. '''
    level = 0
    pos = []
    branches = []
    
    for i in range(len(t)):
        if t[i] == '(':
            level += 1
            pos.append(i)
        elif t[i] == ')':
            s = t[pos[-1]+1:i]
            del pos[-1]

            while len(branches) < level:
                branches.append([])
                
            branches[level-1].append(s)
            level -= 1

    return branches[::-1]
    
    
def offspring_prob(parents):
    ''' Calculate the probability that the offspring will exhibit the 'AA', 
        'Aa', or 'aa' genotype, based on the probability that each of the 
        parents do. 
    '''
    
    # Split the two branches of the subtree.
    if parents[0] == '(':
        level = 1
        i = 1
        
        while level > 0:
            if parents[i] == '(':
                level += 1
            elif parents[i] == ')':
                level -= 1
            i += 1
                
        a, b = parents[:i], parents[i+1:]
                
    else:
        a, b = parents.split(',')
    
    # The probability of each parent possessing each genotype.
    p1, p2 = prob[a], prob[b]
    
    # Initialize the probability of the offspring possessing each genotype.
    offspring = prob['(' + a + ',' + b + ')'] = [0, 0, 0]
    
    # Probability offspring being homozygous dominant.
    offspring[0] += p1[0] * p2[0]                                   # p(AA x AA)
    offspring[0] += (p1[0] * p2[1] * 0.5) + (p1[1] * p2[0] * 0.5)   # p(AA x Aa)
    offspring[0] += p1[1] * p2[1] * 0.25                            # p(Aa x Aa)
    
    # Probability offspring being heterozygous.
    offspring[1] += (p1[0] * p2[1] * 0.5) + (p1[1] * p2[0] * 0.5)   # p(AA x Aa)
    offspring[1] += (p1[0] * p2[2]) + (p1[2] * p2[0])               # p(AA x aa)
    offspring[1] += p1[1] * p2[1] * 0.5                             # p(Aa x Aa)
    offspring[1] += (p1[1] * p2[2] * 0.5) + (p1[2] * p2[1] * 0.5)   # p(Aa x aa)
    
    # Probability offspring being homozygous recessive.
    offspring[2] += p1[1] * p2[1] * 0.25                            # p(Aa x Aa)
    offspring[2] += (p1[1] * p2[2]) * 0.5 + (p1[2] * p2[1] * 0.5)   # p(Aa x aa)
    offspring[2] += p1[2] * p2[2]                                   # p(aa x aa)
    
    return offspring

    
def pedigree(tree):
    ''' Iteratively calculate the genotype probabilities for the offspring of 
        each ancestor pair in the tree, down to the root. 
    '''
    for tree_level in subtrees(tree):
        for pair in tree_level:
            prob = offspring_prob(pair)
            
    return prob


if __name__ == '__main__':
    # Initialize a dictionary to hold the genotype probability of each ancestor.
    prob = {'AA':[1, 0, 0], 'Aa':[0, 1, 0], 'aa':[0, 0, 1]}
    
    # Read the Newick tree.
    with open('problem_datasets/rosalind_mend.txt', 'r') as infile:
        tree = infile.read().strip()
        
    # Calculate the genotype probabilities for the individual at the tree root.
    print(' '.join(map(str, pedigree(tree))))
