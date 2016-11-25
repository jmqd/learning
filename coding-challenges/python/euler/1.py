"""
Find the sum of all the multiples of 3 or 5 below 1000.
"""
import argparse

def init():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", '--up_to', help='The integer N up to which to' +
            ' sum all multiples of 3 or 5.', required = True, type = int)
    return parser.parse_args()

def main():
    args = init()
    print(solve(args.up_to))

def solve(n):
    multiples = (x for x in range(n) if x % 3 == 0 or x % 5 == 0)
    return sum(multiples)

main()
