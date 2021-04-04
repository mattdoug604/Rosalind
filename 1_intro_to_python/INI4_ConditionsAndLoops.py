#!/usr/bin/env python3
# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.

a = 4280
b = 8733

s = 0

for x in range(a, b + 1):
    if x % 2 == 1:
        s += x

print(s)
