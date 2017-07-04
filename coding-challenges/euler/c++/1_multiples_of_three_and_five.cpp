// Find the sum of all the multiples of 3 or 5 below 1000.
#include<iostream>

int brute_force(int n) {
    int sum = 0;
    for (int i = 3; i < n; ++i) 
    {
        if (i % 3 == 0 || i % 5 == 0) 
        {
            sum += i;
        }
    }
    return sum;
}

/*
 * Can solve this problem using math.
 * n * (n + 1) / 2 is the geometric series 1 + 2 + 3 + 4 + ...
 *
 * Just produce that series up to n / k and muliply it by k,
 * summing the series...
 */
int geometric_sum(int k, int n)
{
    return k * ((n - 1)/k) * (((n - 1)/k + 1) / 2);
}

int main()
{
    std::cout << "Enter an integer up to which to sum 3s and 5s. > ";
    int n = 0;
    std::cin >> n;

    int sum = geometric_sum(3, n) + geometric_sum(5, n);
    std::cout << '\n' << sum << '\n';
    return 0;
}
