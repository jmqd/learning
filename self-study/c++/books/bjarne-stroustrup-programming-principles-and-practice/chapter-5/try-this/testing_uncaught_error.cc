// Sees what happens if an error isn't caught.

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<regex>
#include<map>

void error(std::string s1, std::string s2)
{
    throw std::runtime_error(s1 + s2);
}

int main()
{
    std::string input_int = "";

    std::cout << "Enter an integer > ";
    std::cin >> input_int;
    std::string pattern = "[0-9]{1,}";
    std::regex regexp = std::regex(pattern);
    if (!std::regex_match(input_int, regexp))
    {
        std::string s1 = "",
                    s2 = "";
        error(s1, s2);
    }
    else
    {
        std::cout << "\nAll is well.\n";
    }
}
