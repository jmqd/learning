// Modify program from previous exercise to allow querying
// by username at the end.

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

    std::string query = "";
    std::cout << "\nEnter a name to find their age > ";
    std::cin >> query;
    auto query_result = std::find(names.begin(), names.end(), query);
    if (query_result != names.end())
    {
        int age_index = query_result - names.begin();
        std::cout << query << " is " << ages[age_index] << " years old.";
    }
    else 
    {
        std::cout << "Sorry, I couldn't find " << query << " in the agebook.";
    }
}
