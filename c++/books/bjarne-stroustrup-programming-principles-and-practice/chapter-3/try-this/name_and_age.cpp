// This file was constructed from a template designed for the first few
// chapters of the book to save time. It may be the case that some of these
// includes are unnecessary. That's okay.

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
inline void keep_open() {char ch; std::cin >> ch;}

int main()  // C++ programs start by executing the main function
{
    // vars
    std::string first_name = "";
    // double for kids who are very proud of being five and a half
    double age = 0;
    std::cout << "Please enter your name.\n";
    std::cin >> first_name;
    std::cout << "Please enter your age.\n";
    std::cin >> age;
    std::cout << "Hello, " << first_name << " (age " << age << ")\n";
}
