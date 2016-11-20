/*
 * Given an integer n, enumerate all primes up to n.
 * THIS IS THE INITIAL BRUTE FORCE SOLUTION.
 */

#include<vector>
#include<iostream>

bool is_prime(int num)
{
    if (num == 1) { return false; } 
    if (num == 2) { return true; }

    for (int i = 2; i * i <= num; ++i)
    {
        if (num % i == 0) { return false; }
    }
    return true;
}

std::vector<int> primes_to_n(const int n)
{
    std::vector<int> primes;

    for (int i = 2; i <= n; ++i)
    {
        if (is_prime(i)) { primes.push_back(i); }
    }
    return primes;
}

void test()
{
    int n = 0;
    std::cout << "Please enter an integer n > ";
    std::cin >> n;
    for (int i: primes_to_n(n))
    {
        std::cout << '\n' << i;
    }
    std::cout << '\n';
}

int main()
{
    test();
    return 0;
}
