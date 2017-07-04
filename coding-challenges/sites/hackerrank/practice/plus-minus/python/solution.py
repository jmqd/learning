#!/bin/python
from __future__ import print_function, division
from collections import defaultdict

'''
Very simple little problem...

1. Read from STDIN n (num of cases), and arr, space separated integers.
2. Print out the proportions of zeroes, negatives, and positives on three
	lines.
'''

# read in test case stuff from STDIN
n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

# build stats dict
statistics = defaultdict(int)

for elem in arr:
    if elem == 0: statistics[0] += 1
    elif elem < 0: statistics['-'] += 1
    elif elem > 0: statistics['+'] += 1

map(lambda x: print(statistics[x] / n), ['+', '-', 0])
