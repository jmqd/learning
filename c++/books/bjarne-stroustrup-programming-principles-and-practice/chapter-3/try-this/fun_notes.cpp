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
    int a = 0;
    int b = 0;
    std::cout << "let a = ";
    std::cin >> a;
    std::cout << "let b = ";
    std::cin >> b;
    std::cout << "Doing a / b * b + a \% b...\n";
    std::cout << "a: " << a << std::endl << "b: " << b << std::endl;
    int result = a / b * b + a % b;
    std::cout << "a / b * b + a \% b == " << result << std::endl;
    std::cout << "equality test: "  << (a == result) << std::endl;
}
