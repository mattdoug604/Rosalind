#!/usr/bin/env python3
"""
Compute the number of peptides of given total mass.
Given: An integer m.
Return: The number of linear peptides having integer mass m.
"""
"""
def permu(m, masses):  
    ways = [0] * (m + 1)
    ways[0] = 1
    for mass in mass_list:
        for j in range(mass, m + 1):
            ways[j] += ways[j - mass]
    return ways[m]

print(permu(mass, mass_list))
"""
try:
    import psyco

    psyco.full()
except ImportError:
    pass


def count_changes(amount_cents, coins):
    n = len(coins)
    # max([]) instead of max() for Psyco
    cycle = max([c + 1 for c in coins if c <= amount_cents]) * n
    table = [0] * cycle
    for i in range(n + 1):
        table[i] = 1

    pos = n
    for s in range(1, amount_cents + 1):
        for i in range(n):
            if i == 0 and pos >= cycle:
                pos = 0
            if coins[i] <= s:
                q = pos - coins[i] * n
                table[pos] = table[q] if (q >= 0) else table[q + cycle]
            if i:
                table[pos] += table[pos - 1]
            pos += 1
    return table[pos - 1]


def main():
    mass = 1024
    mass_list = [
        57,
        71,
        87,
        97,
        99,
        101,
        103,
        113,
        113,
        114,
        115,
        128,
        128,
        129,
        131,
        137,
        147,
        156,
        163,
        186,
    ]

    print(count_changes(mass, mass_list))


main()
