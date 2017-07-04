/*
 * Given an integer n, enumerate all primes up to n.
 * This is the second approach to this problem -- a sieved version.
 * Specifically, I believe this is the 'Sieve of Eratosthenes'.
 *
 * After some reading, it seems the time complexity of this algorithm
 * is O(n log log n), although this is not obvious or trivial to me.
 *
 * Its space complexity is O(n).
 */

#include<vector>
#include<iostream>

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

void test()
{
    int n = 0;
    std::cout << "Please enter an integer n > ";
    std::cin >> n;
    std::vector<bool> sieve_vector = primes_to_n(n);

    // outputting the primes. skipping 0 because I didn't bother setting
    // its value in the vector to false
    for (int i = 1; i <= n; ++i)
    {
        if (sieve_vector[i]) { std::cout << i << '\n'; }
    }
}

int main()
{
    test();
    return 0;
}
