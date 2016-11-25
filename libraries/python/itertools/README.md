# itertools study

---

## Some notes...

### _Some of this may be python3 specific. That's okay._

- operator module
 - provides functional versions of all of the operators (add, subtract,
 less than, greater than, etc.)
 - e.g. `from operator import add`

- functools
 - `from functools import partial`
  - partial function application ("currying")
  - `def add1(x): return add(1, x)` could be written as
  `add1 = partial(add, 1)`
 - `from functools import reduce`

- iterators
 - something you can call next() on and get values one at a time

```
In [1]: xs = [1, 2, 3]
In [2]: it = iter(xs)
In [3]: next(it)
Out [3]: 1
In [4]: next(it)
Out [4]: 2
In [5]: next(it)
Out [5]: 3
In [6]: next(it)
StopIteration Exception
```

 - setting up valyes one-at-a-time with next() means you can generate them
 on-demand _(laziness)_
 - allows us to create lazy infinite sequences
 - laziness is one of the hallmarks of functional programming

- generators
 - function with yield creates a generator
 - when you call next(), it will evaluate lazy_integers until it sees yield,
 then it will pause and remember where it is. Then, when you call next() again,
 it will continue where it left off until it sees another yield.

```
def lazy_integers(n = 0):
    while True:
        yield n
        n += 1

xs = lazy_integers()

[next(xs) for _ in range(10)]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# maintains state
[next(xs) for _ in range(10)]
# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```

## generator comprehensions

```
# computes nothing until next or for
squares = (x**2 for x in lazy_integers())
doubles = (2*x for x in lazy_integers())
```

## consider this: generators as pipelines

_(Unix command line way of counting occurences of prime in haskell file)_
`cat euler.hs | grep -i prime | wc -l`

### python generator approach

```
with open('euler.hs', 'r') as f:
    lines = (line for line in f)
    prime_lines = filter(lambda line: 'prime' in line.lower(), lines)

    # make sure to force evaluation before f goes out of scope!
    # or else ValueError: I/O operation on closed file
    line_count = len(list(prime_lines))
```

- `from itertools import count`
 - `count([start = 0], [step = 1])`
  - gives this infinite sequence: start, start + step, start + 2 * step, ...

- `from itertools import islice`
 - `islice(seq, [start = 0], stop, [step = 1])`
 - returns a "lazy slice" out of seq.

- `from itertools import tee`
 - `tee(it, [n = 2])`
 - splits an iterator into two or more _memoized_ copies.
 - huge efficiency gains if you have to iterate through expensive computations
 multiple times

- `from itertools import repeat`
 - `repeat(elem, [n = forever])`
 - repeats elem n times (or forever if no n)

- `from itertools import cycle`
 - `cycle(p)`
 - repeats the elements of p over and over and over again forever

- `from itertools import chain`
 - `chain(p, q, ...)`
 - iterates through the elements of p, then the elements of q, and so on

- `from itertools import accumulate`
 - `accumulate(p, [func = add])`
 - returns the sequence a, where:

```
a[0] = p[0]
a[1] = func(a[0], p[1])
a[2] = func(a[1], p[2])
```

## we need some itertools of our own

```
# force the first n values of a sequence
def take(n, it):
    return [x for x in islice(it, n)]

# new sequence with all but the first n values of a sequence
def drop(n, it):
    return islice(it, n, None)

# force the first value of a sequence
head = next

# new sequence with all but the first value of a sequence
tail = partial(drop, 1)
```

- we're also missing `iterate`
 - `iterate(f, x)`
  - should be: `x, f(x), f(f(x)), ...`

```
def iterate(f, x):
    return accumulate(repeat(x), lambda fx, _: f(fx))
```

## using iterate

```
def lazy_integers():
    return iterate(add1, 0)

take(10, lazy_integers())
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### fibonacci numbers

#### _naive level 0 approach_

```
def fib(n):
    if n in (0, 1): return 1
    return fib(n - 1) + fib(n - 2) # super inefficient; for example only

[fib(i) for i in range(10)]
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

#### _second iteration_

```
def fibs():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b # efficient-ish, but look at the gross mutation

take(10, fibs())
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

#### _third iteration, using tee_

```
def fibs():
    yield 1
    yield 1
    fibs1, fibs2 = tee(fibs())
    yield from map(add, fibs1, tail(fibs2))
```

_Fairly efficient, using the memoized values, but feels clunky..._

#### _fourth iteration, getting more functional..._

```
def next_fib(pair):
    x, y = pair
    return (y, x + y)

def fibs():
    return (y for x, y in iterate(next_fib, (0, 1)))
```

_Good functional approach, and quite efficient._

