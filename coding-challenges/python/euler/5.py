"""
What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?
"""


def prime_factors(num):
    i = 2
    factors = []
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return factors

def main():
    # initialization
    up_to = 20
    result = 1
    sequence = {key: 0 for key in range(1, up_to + 1)}

    for num in range(1, up_to + 1):
        primes = prime_factors(num)
        for factor in primes:
            count = primes.count(factor)
            if count > sequence[factor]:
                sequence[factor] = count
        if len(primes) > 1:
            del sequence[num]

    for key, value in sequence.items():
        if value == 0:
            continue
        else:
            result *= key ** value

    print(result)

if __name__ == '__main__':
    main()
