#!/usr/bin/python

# Compute the number of peptides of given total mass.
# Given: An integer m.
# Return: The number of linear peptides having integer mass m.

mass = 1024

def permu(m):
    mass_list = [ 57, 71, 87, 97, 99, 101, 103, 113, 113, 114,
               115, 128, 128, 129, 131, 137, 147, 156, 163, 186 ]
    
    for i in range(len(mass_list)):
        sum = 0
