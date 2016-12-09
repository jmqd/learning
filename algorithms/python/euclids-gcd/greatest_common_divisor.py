def gcd(n, m):
    '''Very simple algorithm to find the GCD of two numbers.

    Using this algorithm as a vehicle for the analysis of behavior in CS.

    How do we describe a set of behaviors?
        - There's a theorem that says that any set B of behaviors is the
        intersection of two sets -- a set of behviors satisfying a safety
        property and a set of behaviors satisfying a liveness property.

        So what are safety and liveness?

        [Informal definitions...]

        Safety property:
            - False if and only if it can be violated at some point during the
            behavior. (i.e. It is invariant.)
                e.g. "partial correctness" -- violated if program stops w/ the
                wrong answer.
        Liveness property:
            - need to see the complete behavior in order to know if it's false
            or satisfied by the program.
            - classic example: termination. you cannot tell that the program
            hasn't terminated by looking at any finite piece of the program.
            you have to look at the entire behavior to know that it never
            terminates.

        So now we describe the behavior of a program in terms of these two
        sets... It turns out that specifying the safety property is more
        important...
            - it's where most errors are likely to occur (and tend to be more
            subtle.

        How to specify a safety property:
            - the set of possible initial states
            - the next-state relation, describing all possible successor states
                of any given state.

        Set of initial states:
            (For Euclid's algorithm, as shown below.):
                (x = m) ^ (y = n)
                Only possible initial state: [x = m, y = n]

        The next-state relation:
            (Note: unprimed variables for current state; primed variables for
                next state.)

            Two possibilities, either m > n or n > m:
                (  m > n
                 ^ m' = m - n
                 ^ n' = n)
             OR (  n > m
                 ^ n' = n - m
                 ^ m' = m)
    '''
    if any(i < 1 for i in (n, m)): return None
    if n == m: return n
    else:
        n, m = n - m, m if n > m else m - n, n
        return gcd(n, m)
