#!/usr/bin/env python3

"""
Rosalind: Bioinformatics Stronghold
Problem: Distances in Trees
URL: http://rosalind.info/problems/nwck/

Given: A collection of n trees (n <= 40) in Newick format, with each tree
containing at most 200 nodes; each tree Tk is followed by a pair of nodes xk 
and yk in Tk.
Return: A collection of n positive integers, for which the kth integer
represents the distance between xk and yk in Tk.
"""


def find_lca(t, a, b):
    """Find the lowest common ancestor of both nodes being compared. Returns
    a partially complete list (unless the LCA is the root of the tree) of
    each level of the tree that contains the LCA, and the level of the
    tree containing the LCA.
    """
    level = 0
    pos = []
    subtrees = []

    for i in range(len(t)):
        if t[i] == "(":
            level += 1
            pos.append(i)
        elif t[i] == ")":
            sub = t[pos[-1] + 1 : i]
            del pos[-1]

            while len(subtrees) < level:
                subtrees.append([])

            subtrees[level - 1].append(sub)
            level -= 1

            if a in sub and b in sub:
                return (subtrees, level)

    return subtrees, level


def distance_to_lca(lca, node):
    """ Returns the distance from a given node to the LCA. """
    binary = False
    binary_weight = lambda binary: 1 if binary else 2

    for i in range(len(lca)):
        includes_node = False

        for sub in lca[i]:
            if "," in sub:
                binary = True

            if node in sub:
                includes_node = True
                break

        if includes_node == False:
            dist = i - binary_weight(binary)
            return dist

    dist = len(lca) - binary_weight(binary)

    return dist


def distance_between_nodes(t):
    """ Finds the pairwise distance between two nodes in a rooted tree. """
    tree = t[0]
    a, b = t[1].split(" ")

    subtrees, lca = find_lca(tree, a, b)
    dist = 2 + distance_to_lca(subtrees[lca:], a) + distance_to_lca(subtrees[lca:], b)

    return dist


def main():
    with open("problem_datasets/rosalind_nwck.txt", "r") as infile:
        trees = [l.split("\n") for l in infile.read().strip().split("\n\n")]

    print(" ".join([str(distance_between_nodes(t)) for t in trees]))


if __name__ == "__main__":
    main()
