#include<iostream>

/*
 * We can solve this with mathematics.
 *
 * n * (n + 1) / 2 is the geometric series 1 + 2 + 3 + ...
 *
 * We must construct this series for mutiples of k by multiplying
 * the series by k. Then we can construct our sum by calling
 * this function like so: geo_sum(3) + geo_sum(5) - geo_sum(15)
 */
long geometric_sum(int k, long n)
{
    return k * (n / k) * ((n / k) + 1) >> 1;
}

int main()
{
    int n = 0;
    std::cin >> n;
    for (int i = 0; i < n; ++i) {
        long num = 0;
        std::cin >> num;

        // problem only asks for things below the num
        --num;

        long sum =
              geometric_sum(3, num)
            + geometric_sum(5, num)
            - geometric_sum(15, num);

        std::cout << sum << '\n';
    }
}

