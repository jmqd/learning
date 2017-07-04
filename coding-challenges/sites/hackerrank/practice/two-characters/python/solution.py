#!/bin/python
from __future__ import print_function
import itertools

'''
This solution feels slightly hacky. I speculate a much better solution exists.
'''

s_len = int(raw_input().strip())
s = raw_input().strip()

def solve(s):
    chars = set(s)
    pairs = itertools.combinations(chars, 2)
    largest_possible = 0

    for pair in pairs:
        last_char = None
        current_size = 0
        for char in s:
            if char in pair and last_char != char:
                last_char = char
                current_size += 1
            elif last_char == char:
                current_size = 0
                break
        if current_size > largest_possible:
            largest_possible = current_size

    print(largest_possible)

def main():
    solve(s)

if __name__ == '__main__':
    main()
