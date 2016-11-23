// Write a program that is a naive letter generator.
//

#include<iostream>
#include<string>
#include<array>
#include<vector>
#include<algorithm>
#include<cmath>
inline void keep_open() {char ch; std::cin >> ch;}

int main()
{
    // initialization
    char operation = '\0';
    double operand1 = 0.0;
    double operand2 = 0.0;
    double result = 0.0;

    // inputs
    std::cout << "Please enter an expression to be evaluated in RPN.\n";
    std::cin >> operation >> operand1 >> operand2; 

    // logic
    switch (operation)
    {
        case '*':
            result = operand1 * operand2;
            break;
        case '+':
            result = operand1 + operand2;
            break;
        case '-':
            result = operand1 - operand2;
            break;
        case '/':
            result = operand1 / operand2;
            break;
    }
    
    // outputs
    std::cout << result;
}
