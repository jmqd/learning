// Modify the previous program to find the prime numbers from 1 to N.

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
    int n = 0;
    std::cout << "Finding prime numbers from 1 up to ... > ";
    std::cin >> n;
    for (int i = 1; i < n + 1; ++i)
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
