#!/usr/bin/env python3
"""
Given: Two positive integers a and b, each less than 1000.
Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.
"""

import math

a = 945
b = 817
print(int(math.pow(a, 2) + math.pow(b, 2)))
