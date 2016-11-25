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
    std::string text = "";
    std::cout << "Enter an integer i such that 0 <= i < 10 in text form.\n";
    std::cin >> a;
    switch (a)
    {
        case 0:
            text = "zero";
            break;
        case 1:
            text = "one";
            break;
        case 2:
            text = "two";
            break;
        case 3:
            text = "three";
            break;
        case 4:
            text = "four";
            break;
        case 5:
            text = "five";
            break;
        case 6:
            text = "six";
            break;
        case 7:
            text = "seven";
            break;
        case 8:
            text = "eight";
            break;
        case 9:
            text = "nine";
            break;
        default:
            text = "not a number I know.";
    }
    if (text != "not a number I know.") {
        std::cout << "The text for " << a << " is " << text;
    } else {
        std::cout << text;
    }

}
