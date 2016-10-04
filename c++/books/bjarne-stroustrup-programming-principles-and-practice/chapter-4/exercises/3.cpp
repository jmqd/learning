// Read a sequence of double values into a vector.
// Think of each value as the distance between two cities along a given route.
// 1. Compute and print the total distance.
// 2. Find the smallest and the greatest distance between two neighbor cities.
// 3. Find and print the mean distance between cities.

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>

double sum(std::vector<double> values)
{
    double total = 0.0;
    for (double v: values)
    {
        total += v;
    }
    return total;
}

double max(std::vector<double> values)
{
    double max_dist = std::numeric_limits<double>::min();
    for (double i: values)
    {
        if (i > max_dist)
        {
            max_dist = i;
        }
    }
    return max_dist;
}

double min(std::vector<double> values)
{
    double min_dist = std::numeric_limits<double>::max();
    for (double i: values)
    {
        if (i < min_dist)
        {
            min_dist = i;
        }
    }
    return min_dist;
}

double mean(std::vector<double> values)
{
    double rolling_sum = 0.0;
    for (double i: values)
    {
        rolling_sum += i;
    }
    return rolling_sum / values.size();
}

int main()
{
    std::cout << "Give me some distances!\n";
    std::vector<double> values;

    for (double value; std::cin >> value; )
    {
        values.push_back(value);
    }
    
    std::cout << "\nMax dist is: \t" << max(values);
    std::cout << "\nMin dist is: \t" << min(values);
    std::cout << "\nMean dist is: \t" << mean(values);
}
