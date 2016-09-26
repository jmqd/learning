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
    // initializations
    double input_value = 0.0;
    double result = 0.0;
    char input_mode = '\0';
    std::string unit_pronoun = "";

    while (input_mode != 'm' && input_mode != 'k')
    {
        std::cout << "Welcome to the miles and kilometers converter.\n"
            "Enter your source unit. 'm' for miles, 'k' for kilometers.\n";
        std::cin >> input_mode;
    }
    unit_pronoun = (input_mode == 'm') ? "miles" : "kilometers";
    std::string target_pronoun = (input_mode == 'm') ? "kilometers" : "miles";
    std::cout << "Enter the number of " + unit_pronoun + " to convert.\n";
    std::cin >> input_value;


    // processing
    double mult = (input_mode == 'm') ? 1.60934 : 0.62137273665;
    result = input_value * mult;
    // output
    std::cout << input_value << " " << unit_pronoun << " is:\n";
    std::cout << result << " " << target_pronoun;
}
