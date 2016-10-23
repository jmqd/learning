// Modify program from previous exercise to allow querying
// by age at the end.

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<regex>
#include<map>

int main()
{
    std::vector<std::string> names;
    std::vector<int> ages;
    std::string name = "";
    int age = 0;

    std::cout << "\nBook of names and ages.\n";
    std::cout << "===========================================================";
    std::cout << "\nInput is terminated by entering END";
    std::cout << "\nEnter some name age pairs, like so: Joe 5 Jordan 23 etc\n";
    while (std::cin >> name && name != "END")
    {
        names.push_back(name);
        std::cin >> age;
        ages.push_back(age);
    }

    for (int i = 0; i < names.size(); ++i)
    {
        std::cout << names[i] << " is " << ages[i] << " years old.\n";
    }

    int query = 0;
    std::cout << "\nEnter an age to find names w/ that age > ";
    std::cin >> query;
    std::vector<std::string> query_results;

    for (int i = 0; i < ages.size(); ++i)
    {
        if (ages[i] == query)
        {
            query_results.push_back(names[i]);
        }
    }

    if (query_results.size() == 0)
    {
        std::cout << "Sorry, I couldn't find " << query << " in the agebook.";
        return 0;
    }

    std::cout << "Names with that age\n";
    std::cout << "===========================================================";
    for (std::string j: query_results)
    {
        std::cout << "\n" << j;
    }
}
