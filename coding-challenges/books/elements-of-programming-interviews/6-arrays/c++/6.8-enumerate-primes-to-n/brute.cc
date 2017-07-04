/*
 * Given an integer n, enumerate all primes up to n.
 * THIS IS THE INITIAL BRUTE FORCE SOLUTION.
 *
 * This algorithm performs sqrt(n) operations n times,
 * so its time complexity is:
 * O(n * sqrt(n))
 * => O((n**1) * (n ** (1/2)))
 * => O(n ** (3/2))
 *
 * Its space complexity: O(1)
 */

#include<vector>
#include<iostream>

bool is_prime(const int num)
{
    switch (num)
    {
        case 1:
            return false; // 1 is excluded as a prime
            break;
        case 2:
            return true; // 2 is a prime number
            break;
        default:
            for (int i = 2; i * i <= num; ++i)
            {
                if (num % i == 0) { return false; }
            }
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
