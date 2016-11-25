// Write a program where you first enter a set of name:value pairs, such as:
// Jordan 23 and Leah 27. For each pair, add the name to a vector called
// names and the number to a vector called ages (in corresponding positions)
// so that if names[7] == "Jordan", then ages[7] == 23. Terminate input with
// NoName 0. Check that each name is unique and terminate with an error message
// if a name is entered twice. Write out all the (name, age) pairs, one per
// line.

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
}
