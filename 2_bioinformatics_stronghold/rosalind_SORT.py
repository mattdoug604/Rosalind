#!/usr/bin/env python3
"""
Rosalind: Bioinformatics Stronghold
Problem: Sorting by Reversals
URL: http://rosalind.info/problems/sort/

Given: Two permutations π and γ, each of length 10.
Return: The reversal distance drev(π,γ), followed by a collection of reversals
sorting π into γ. If multiple collections of such reversals exist, you may
return any one.
 
Input:
1 2 3 4 5 6 7 8 9 10
1 8 9 3 2 7 6 5 4 10

Output:
2
4 9
2 5
"""


def breakpoint(p):
    """Returns a list of elements in the given permutation where a breakpoint
    occurs.
    """
    bp = []

    for i in range(1, len(p)):
        if abs(p[i] - p[i - 1]) > 1:
            bp.append(i)

    return bp


def printRound(p, a, b):
    """Optional: format and print the current reversal."""
    if 10 in p[a:b]:
        x = 1
    else:
        x = 2

    print(p, " - ", "(", a, ",", b - 1, ")", sep="")
    print(" ", " " * (a * 3), "-" * ((b - a) * 3 - x), sep="")


def reversal_dist(p1, p2):
    """Determine the minimum reversal distance for a pair of permutations by
    performing a greedy search. Returns a dictionary of the minimum reversal
    distance and the reversals need to achieve that. If there's more than
    one solution, it just returns the first one.
    """

    # Perform a quick check to see if the pair is already the same.
    if p1 == p2:
        return 0

    # Prepend 0 and append len(permutation)+1 to determine if endpoints are
    # correct.
    p_start = [0] + [p1.index(x) + 1 for x in p2] + [len(p1) + 1]

    # Set the starting conditions.
    count = 0
    reversal_list = [[[p_start, count]]]
    bp_min = len(breakpoint(p_start))

    # The maximum required number of reversals to solve this is
    # len(permutation) + 1, so loop until we hit that mark, or solve the
    # problem.
    while count < len(p_start) + 1:
        reversal_list.append([])
        new_reversals = []

        for perm_item in reversal_list[count]:
            perm = perm_item[0]
            revs = perm_item[2:]
            bp = breakpoint(perm)

            # Reverse each pair of breakpoints.
            for i in range(len(bp)):
                for j in range(i + 1, len(bp)):
                    a = bp[i]
                    b = bp[j]
                    if b - a > 1:

                        p_new = perm[:a] + list(reversed(perm[a:b])) + perm[b:]
                        bp_new = len(breakpoint(p_new))

                        if len(perm_item) > 2:
                            revs = perm_item[2:][0] + [a] + [b - 1]
                        else:
                            revs = [a, b - 1]

                        # Problem solved when no breakpoints remain. The
                        # reversal(s) with the least breakpoints is/are the best
                        # choice in this case, so we can throw out the others.
                        if bp_new == 0:
                            return p_new, count + 1, revs
                        elif bp_new < bp_min:
                            bp_min = bp_new
                            reversal_list[count + 1] = []
                            reversal_list[count + 1].append([p_new, count + 1, revs])
                        elif bp_new == bp_min:
                            reversal_list[count + 1].append([p_new, count + 1, revs])

        count += 1


def checkAnswer(to_match, to_reverse, revs):
    """Go through the reversals in the list to see if the permutations end up
    the same (i.e. make sure the answer if correct).
    """
    temp = to_reverse
    for i in range(0, len(revs), 2):
        a = revs[i] - 1
        b = revs[i + 1]

        printRound(temp, a, b)
        temp = temp[:a] + list(reversed(temp[a:b])) + temp[b:]

    if temp == to_match:
        print(temp, "<-- Correct Match!\n")
    else:
        print(temp, "<-- Incorrect Match!\n")


def main():
    # Read the input .txt file.
    with open("problem_datasets/rosalind_sort.txt", "r") as infile:
        pair = infile.read().strip().split("\n")
        permA, permB = [list(map(int, p.split(" "))) for p in pair]

    # Get the reversal distances.
    perm, count, revs = reversal_dist(permA, permB)

    # Optional: check make sure the revesals end up with the correct permutations.
    # checkAnswer(permA, permB, revs)

    # Print the answer.
    print(count)
    for i in range(len(revs), 0, -2):
        print(revs[i - 2], revs[i - 1])


if __name__ == "__main__":
    main()
