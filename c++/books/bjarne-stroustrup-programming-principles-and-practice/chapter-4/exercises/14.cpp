// Use the Sieve of Eratosthenes to find the prime numbers from 1 to N.

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<regex>
#include<map>

int main()
{
    // initializations
    int v_length = 101;
    std::vector<bool> number_grid(v_length, true);

    // user inputs
    std::cout << "Enter the N to which to use the sieve to find primes. > ";
    std::cin >> v_length;

    // ugly, I know...
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
    for (int i = 1; i < v_length; ++i)
    {
        if (number_grid[i])
        {
            std::cout << i << '\n';
        }
    }
}
