#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>

int main()
{
    std::cout << "Gives the median of an array.\n";
    std::vector<double> values;

    for (double value; std::cin >> value; )
    {
        values.push_back(value);
    }
    
    int mid = (values.size() - 1 ) / 2;

    if (values.size() % 2 == 0)
    {
        std::cout << "\nMedian is " << (values[mid] + values[mid + 1]) / 2;
        std::cout << '\n';
    }

    if (values.size() % 2 != 0)
    {
        std::cout << "\nMedian is " << values[mid] << '\n';
    }
}
