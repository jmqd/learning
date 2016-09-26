// Write a program that is a naive letter generator.
//
// TODO:
//  - make it to accept whole line of input.

#include<iostream>
#include<string>
#include<array>
#include<vector>
#include<algorithm>
#include<cmath>
inline void keep_open() {char ch; std::cin >> ch;}

int main()
{
    int a = 0;
    int b = 0;
    std::cout << "Enter an integer.\nLet a = ";
    std::cin >> a;
    std::cout << "Enter an integer.\nLet b = ";
    std::cin >> b;

    double ratio_a_to_b = (double) a / (double) b;
    double ratio_b_to_a = (double) b / (double) a;

    std::string comparison =
        (a > b)
        ? "a is greater than b"
        : "b is greater than a";
    
    std::cout << comparison << '\n'
        << "a + b is " << a + b << '\n'
        << "a - b is " << a - b << '\n'
        << "b - a is " << b - a << '\n'
        << "b * a is " << b * a << '\n'
        << "the ratio of b:a is " << ratio_b_to_a << '\n'
        << "the ratio of a:b is " << ratio_a_to_b << '\n';
}
