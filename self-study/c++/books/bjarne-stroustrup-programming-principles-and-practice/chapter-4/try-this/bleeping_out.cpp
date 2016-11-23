#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>

int main()
{
    std::vector<std::string> words;
    std::cout << "\nEnter some words to be filtered\n> ";
    for (std::string temp; std::cin >> temp; )
    {
        words.push_back(temp);
    }

    for (std::string word: words)
    {
        if (word == "yardwork" || word == "chores" || word == "gardening"
            || word == "weeding")
        {
            std::cout << "BLEEP\n";
        }
        else
        {
            std::cout << word << '\n';
        }
    }
}
