#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Finding the Longest Multiple Repeat
URL: http://rosalind.info/problems/lrep/

Given: A DNA string s (of length at most 20 kbp) with $ appended, a positive
integer k, and a list of edges defining the suffix tree of s. Each edge is
represented by four components:

    1. the label of its parent node in T(s);
    2. the label of its child node in T(s);
    3. the location of the substring t of s∗ assigned to the edge; and
    4. the length of t.

Return: The longest substring of s that occurs at least k times in s. (If
multiple solutions exist, you may return any single solution.)
"""


def longest_substring(s, k, edges):
    """Build a tree from an edge list and find the longest repeat that occurs
    more than k times.
    """

    # Construct a tree from the edge list.
    child = {}
    parent = {}
    for p, c, a, b in edges:
        t = s[int(a) - 1 : int(a) - 1 + int(b)]

        if p in child:
            child[p].append(c)
        else:
            child[p] = [0, c]

        if c in parent:
            parent[c].append(p)
        else:
            parent[c] = [0, t, p]

    # Find the root of the tree.
    for i in child.keys():
        if i not in parent:
            root = i

    # Find the leaves (childless nodes) of the tree.
    leaves = []
    for i in parent.keys():
        if i not in child:
            leaves.append(i)

    # Annotate the levels of the tree (i.e. distance from root).
    p = [root]
    lvl = 1
    while True:
        new_p = []
        for i in p:
            if i in child:
                for j in child[i][1:]:
                    parent[j][0] += lvl
                    new_p.append(j)

        if new_p != []:
            p = new_p
            lvl += 1
        else:
            break

    # Count the number of leaf descendants of each node.
    top_nodes = []
    for i in leaves:
        top = ""
        par = parent[i][2]

        while True:
            child[par][0] += 1

            if child[par][0] >= k:
                if par != root:
                    top_nodes.append(par)

            if par in parent:
                par = parent[par][2]
            else:
                break

    # Find the max depth of the nodes w/ at least k leaf descendants.
    max_depth = max([parent[i][0] for i in top_nodes])

    # ...of those nodes, get the one(s) farthest from the root.
    deep_nodes = []
    for i, j in parent.items():
        if j[0] == max_depth:
            if i not in leaves:
                deep_nodes.append(i)

    # Traceback to the root to build substrings.
    substrings = []
    for i in deep_nodes:
        sub = ""
        par = i
        while True:
            t, par = parent[par][1:]
            sub = t + sub
            if par not in parent:
                substrings.append(sub)
                break

    # Return the longest of the substrings.
    longest = max(substrings, key=len)

    return longest


def main():
    with open("problem_datasets/rosalind_lrep.txt", "r") as infile:
        s = infile.readline().strip()
        k = int(infile.readline().strip())
        edges = [i.strip().split(" ") for i in infile.readlines()]

    print(longest_substring(s, k, edges))


if __name__ == "__main__":
    main()
