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

double calc_square_worth(double square_num)
{
    // binary num
    double grains_of_rice = 1;
    for (double i = 0; i < square_num; ++i)
    {
        grains_of_rice *= 2;
    }
    return grains_of_rice;
}

int calc_squares_required(double grains_desired)
{
    double i = 1;
    double grains = 0;
    while (grains < grains_desired)
    {
        grains += calc_square_worth(i);
        ++i;
    }
    return i - 1;
}

double calc_total_grains(int square)
{
    double answer = 0;
    for (int i = 1; i <= square; ++i)
    { 
        answer += calc_square_worth(i);
    }
    return answer;
}

int main()
{
    double j = 0;
    int i = 0;
    while (!std::isinf(j))
    {
        ++i;
        j = calc_total_grains(i);
        std::cout << "\nFor Square " << i << ", " << j << " grains total.";
    }
    std::cout << "\n===================================";
    std::cout << "\nDoubles break at square " << i << '\n';
    std::cout << "===================================\n";
}
