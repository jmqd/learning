// Write a program that takes an input N and finds the first N primes.

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<regex>
#include<map>

// Suppose Pn to be the nth prime number. The following bounds have been
// shown to be true. [Bach, Eric; Shallit, Jeffrey 1996; Dusart, Pierre (1999)]
//
// log n + log log n - 1 < Pn/n < log n + log log n for n >= 6
//
// From this, we can construct a function to decide how big a sieve to make.
// calc_sieve_size :: (int n) => int k
// calc_sieve_size = n * (log n + log log n) [I'm ignoring < 6]
int calc_sieve_size(int nth_prime)
{
    return nth_prime * (std::log(nth_prime) + std::log(std::log(nth_prime)));
}

int main()
{
    int primes_desired = 0;
    std::cout << "How many prime numbers would you like to see? > ";
    std::cin >> primes_desired;
    int v_length = calc_sieve_size(primes_desired);
    std::vector<bool> number_grid(v_length, true);
    number_grid[0] = false; // zero is not prime
    number_grid[1] = false; // one is not prime

    // sieve of eratosthenes
    for (int i = 2; i < v_length; ++i)
    {
        if (number_grid[i])
        {
            for (int j = 2 * i; j < v_length; j += i)
            {
                number_grid[j] = false;
            }
        }
    }

    // printing output
    int printed = 0;
    int i = 0;
    while (printed < primes_desired)
    {
        if (number_grid[i])
        {
            std::cout << i << '\n';
            ++printed;
        }
        ++i;
    }
}

