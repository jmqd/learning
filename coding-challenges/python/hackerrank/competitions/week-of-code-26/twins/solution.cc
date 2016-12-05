#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

/*
 * Initial approach using sieve. Probably not the best suited for this problem.
 */

bool is_prime(const int n)
{
    if (n == 1) { return false; }
    if (n == 2) { return true; }
    for (int i = 2; i * i <= n; ++i)
    {
        if (n % i == 0) { return false; }
    }
    return true;
}

std::vector<bool> primes_to_n(const int n)
{
    std::vector<bool> sieve_vector(n, true);
    for (int i = 1; i < n; ++i)
    {
        // skip the sieved values (that's the whole point of this algo)
        if (!sieve_vector[n])
        {
            continue;
        }

        // if it's prime, leave it set to true
        if (is_prime(i))
        {
            // but we need to go and make false all of its multiples
            for (int j = 2 * i; i + j < n; j += i)
            {
                sieve_vector[j] = false; 
            }
        }
        // if it's not prime, set it to false
        else
        {
            sieve_vector[i] = false;
        }
    }
    return sieve_vector;
}

int main()
{
    int start = 0,
        end = 0,
        count = 0;
    std::cin >> start >> end;
    
    std::vector<bool> primes = primes_to_n(end);
    
    for (int i = start; i + 2 <= end; ++i)
    {
        if (primes[i] && primes[i + 2])
        {
            ++count;
        }
    }
    std::cout << count;
    return 0;
}

