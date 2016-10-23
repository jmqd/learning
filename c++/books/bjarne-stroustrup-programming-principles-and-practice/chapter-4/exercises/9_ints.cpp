// Try to calculate the number of rice grains the emperor asked for in
// exercise 8. You'll find that the number is so large that it won't fit
// in an int or a double. Observe what happens when the number gets too large
// to represent exactly as an int and as a double. What is the largest number
// of squares for which you can calculate the exact number of grains the (using
// an int)? What is the largest number of squares for which you can calculate
// the approximate number of grains using a double?

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<regex>
#include<map>

int calc_square_worth(int square_num)
{
    // binary num
    int grains_of_rice = 0b1;

    // 2^n can be represented in binary as 1 with n trailing 0s.
    // 2^0 -> 1  ->  0b1
    // 2^1 -> 2  ->  0b10
    // 2^2 -> 4  ->  0b100
    // 2^3 -> 8  ->  0b1000
    // 2^4 -> 16 ->  0b10000
    // ...
    // 1. Incrementing n in the exponent term 2^n is equivalent to (2^n) * 2.
    // 2. Let k = a binary number whose leftmost digit is 1 and all others 0.
    // 3. Appending a 0 to k is equivalent to k - k + 2k.
    // 4. From 3, appending a 0 to k is equivalent to 2*k.
    // 5. Therefore: 2^(n) == 0b1 << n
    return grains_of_rice << (square_num - 1);
}

int calc_squares_required(int grains_desired)
{
    int i = 1;
    int grains = 0;
    while (grains < grains_desired)
    {
        grains += calc_square_worth(i);
        ++i;
    }
    return i - 1;
}

int calc_total_grains(int square)
{
    int answer = 0;
    for (int i = 1; i <= square; ++i)
    { 
        answer += calc_square_worth(i);
    }
    return answer;
}

int main()
{
    int j = 0;
    int i = 0;
    while (j != -1)
    {
        ++i;
        j = calc_total_grains(i);
        std::cout << "\nFor Square " << i << ", " << j << " grains total.";
    }
    std::cout << "\n===================================";
    std::cout << "\nIntegers break at square " << i << '\n';
    std::cout << "===================================\n";
}
