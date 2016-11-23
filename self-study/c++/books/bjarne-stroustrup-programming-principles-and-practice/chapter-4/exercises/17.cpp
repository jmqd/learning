// Write a program that finds the min, max, and mode of a collection
// of strings.

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
    
    std::cout << "I'll get the summary stats of some integers for you.\n"
        "A sequence with multiple modes will return the\n"
        "lexicographically smallest mode.\n";
    std::cout << "===========================================================";
    std::cout << "\nEnter space separated integers, terminated with 'q'.\n";
    // using 'q' to terminate input
    while (std::cin >> input && input != 'q')
    {
        v.push_back(input);
    }
    std::sort(v.begin(), v.end());
    int current_count = 0;
    int max_count = 0;
    int mode;;
    for (int i = 0; i < v.size(); ++i)
    {
        if (i == 0 || v[i - 1] == v[i])
        {
            current_count++;
            if (current_count > max_count)
            {
                max_count = current_count;
                mode = v[i];
            }
        }
        else
        {
            current_count = 1;
        }
    }
    int min = v[0];
    int max = v[v.size() - 1];
    std::cout << "Summary Stats:\n";
    std::cout << "===========================================================";
    std::cout << "\nMin: " << min << '\n';
    std::cout << "Max: " << max << '\n';
    std::cout << "Mode: " << mode << '\n';
}
