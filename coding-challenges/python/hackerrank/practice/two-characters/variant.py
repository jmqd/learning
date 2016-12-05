#!/bin/python
from __future__ import print_function
from collections import Counter

'''Variant: find the maximum string which only contains two distinct chars.

All deletion constraints remain the same, but we can have repeating chars here.
'''


s_len = int(raw_input().strip())
s = raw_input().strip()

def solve(s):
    # using the right tool for the job -- counter
    counter = Counter(s)

    # if the string cannot conform to the requirement to have two chars, return
    if len(counter) < 2:
        print(0)
        return None

    # if memory serves, this method utilizes the heapq module, and heaps
    # are the correct data structure for min or max finding problems
    most_common = counter.most_common(2)
    print(sum(x[1] for x in counter.most_common))


solve(s)
