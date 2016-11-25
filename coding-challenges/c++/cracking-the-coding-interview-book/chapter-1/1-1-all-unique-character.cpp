/*
1. Implement an algorithm to determine if a string has all unique characters.
*/

#include <iostream>
#include <map>
#include <string>

bool check_if_unique(std::string& string)
{
    std::map<char, bool> checked;
    for (char& c : string)
    {
        if (checked.find(c) != checked.end())
        {
            return false;
        }

        checked[c] = true;
    }

    return true;
}


int main()
{
    std::string string;
    std::cout << "Enter a string to check its uniqueness: ";
    std::getline(std::cin, string);

    bool is_unique = check_if_unique(string);

    if (is_unique)
    {
        std::cout << "All chars in string are unique!" << std::endl;;
    }

    if (!is_unique)
    {
        std::cout << "String's chars are not all unique!" << std::endl;
    }
}
