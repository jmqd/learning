// Create a program to find all the prime numbers from 1 to 100 using
// the Sieve of Erathosthenes.

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

    // ugly, I know...
    number_grid[0] = false;
    number_grid[1] = false;

    // sieve of erathosthenes
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
