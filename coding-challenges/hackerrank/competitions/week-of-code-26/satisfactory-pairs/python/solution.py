'''
This solution is the initial brute-force.
It's quite slow and a memory hog, but as far as I can tell, correct.

Thinking of different (read: more efficient) approaches.
'''

import itertools, pprint

def solve(n):
    additions = set()
    pairs = set()
    for i in xrange(1, (n / 2) + 1):
        additions.add((i, n - i))

    for add_pair in additions:
        factors_a = factors(add_pair[0])
        factors_b = factors(add_pair[1])
        for x in itertools.product(factors_a, factors_b):
            if x[0] != x[1]:
                pairs.add((x[0], x[1]) if x[0] < x[1] else (x[1], x[0]))
    return pairs

def factors(num):
    results = []
    i = 1
    while i * i <= num:
        if num % i == 0:
            results.append(i)
            results.append(num / i)
        i += 1
    return results

def hackerrank_solve():
    n = int(raw_input())
    pairs = solve(n)
    print len(pairs)

def test():
    n = 11
    pairs = solve(n)
    pprint.pprint(pairs, indent = 4)
    print len(pairs)

test()
