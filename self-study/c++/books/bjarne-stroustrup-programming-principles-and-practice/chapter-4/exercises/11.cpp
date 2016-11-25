// Create a program to find all the prime numbers between 1 and 100.

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<regex>
#include<map>

bool is_prime(int num)
{
    if (num == 1)
    {
        return false;
    }

    if (num == 2)
    {
        return true;
    }

    for (int i = 2; i <= std::sqrt(num); ++i)
    {
        if (num % i == 0)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    // going to build a naive approach because I noticed that
    // further exercises will apptach a more efficient algorithm

    for (int i = 1; i < 101; ++i)
    {
        std::string result = "";
        bool prime = is_prime(i);

        if (prime)
        {
           result = "prime"; 
        }
        else
        {
            result = "not prime";
        }

        std::cout << i << " is " << result << '\n';
    }
}
