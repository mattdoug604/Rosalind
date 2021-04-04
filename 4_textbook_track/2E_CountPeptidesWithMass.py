#!/usr/bin/env python3
"""
Compute the number of peptides of given total mass.
Given: An integer m.
Return: The number of linear peptides having integer mass m.
"""

m = 224

mass_list = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]


def peptides(n, d):  # eg) 75, dicc
    for mass in mass_list:  # for each possible mass...
        if n - mass in d:  # if n-mass = a mass of an aa...
            d[n] = (
                d.get(n, 0) + d[n - mass]
            )  # d.get(key, default) -> default mass to 0 if not found
    return d


def pep_counter(targ):
    dicc = {0: 1}  # create dictionary of each combination(?)
    min_m = min(mass_list)  # start with smallest mass
    for i in range(targ - min_m + 1):  # 1024 - 57 + 1 = 968
        j = i + min_m  # eg) j = 4 + 71 = 75
        peptides(j, dicc)
    return dicc[targ]  # return last entry in the dicc (i.e. the greatest value)


# This line calls the routine and indexes the returned dict.  Both with the desired mass (the mass we want peptides to sum up to)
print(f"answer: {pep_counter(m)}")
