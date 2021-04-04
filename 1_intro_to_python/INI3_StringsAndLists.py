#!/usr/bin/env python3
# Given: A string s of length at most 200 letters and four integers a, b, c and d.
# Return: The slice of this string from indices a through b and c through d (with space in between), inclusively.

s = "cBVdCLS3x3KitHNiUpj4NP3NzowPOPfN2QXCMdUrKVhj1GnQFKEjBGalKJTYnQ9dNQngParadoxornisAHg4dzpYuyxiRGGoxBV9JTLXnL7ftK1Qb0JU2Qifasciolatam8i9wcdiHST3tQFy9iao9SnjbQmYsTKWokoXRaMBE3gYFoSQz."
a = 68
b = 79
c = 119
d = 128

print(s[a:b+1] + " " + s[c:d+1])
