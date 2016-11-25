// Create a program that finds the mode of a collection of numbers.

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<regex>
#include<map>

int main()
{
    int input = 0;
    std::vector<int> v;
    
    std::cout << "I'll get the mode of some integers for you. A sequence\n"
        "with multiple modes will return the lexicographically smallest mode.";
    std::cout << "\n=======================================================\n";
    std::cout << "\nEnter space separated integers, terminated with 'q'.\n";
    // using 'q' to terminate input
    while (std::cin >> input && input != 'q')
    {
        v.push_back(input);
    }
    std::sort(v.begin(), v.end());
    int current_count = 0;
    int max_count = 0;
    int mode = 0;
    for (int i = 0; i < v.size(); ++i)
    {
        if (i == 0 || v[i - 1] == v[i])
        {
            current_count++;
            if (current_count > max_count)
            {
                max_count = current_count;
                mode = i;
            }
        }
        else
        {
            current_count = 1;
        }
    }
    std::cout << "The mode for that collection of integers is: " << v[mode]
        << '\n';
}
