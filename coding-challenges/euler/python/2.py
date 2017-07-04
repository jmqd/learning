"""
By considering the terms in the Fibonacci sequence whose values
do not exceed four million, find the sum of the even-valued terms.
"""
from itertools import accumulate, repeat

def iterate(f, x):
    return accumulate(repeat(x), lambda fx, _: f(fx))

def main():
    n = 4000000
    print(solve(n))

def solve(n):
    return sum(even_fibs(n))

def even_fibs(n):
    latest = 0
    fibs = generate_fibs()
    while latest < n:
        latest = next(fibs)
        if latest < n and latest % 2 == 0:
            yield latest

def generate_fibs():
    return (y for x, y in iterate(next_fib, (0, 1)))

def next_fib(pair):
    x, y = pair
    return (y, x + y)

if __name__ == '__main__':
    main()
