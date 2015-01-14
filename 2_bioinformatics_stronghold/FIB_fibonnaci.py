#!/usr/bin/python
# -*- coding: utf-8 -*-
# Given: Positive integers n ≤ 40 and k ≤ 5.
# Return: The total number of rabbit pairs that will be present after n months if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

n = 29
k = 4

def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)*k 

print fib(n-1)
# n = 29, k = 4 returns: 170361678269
