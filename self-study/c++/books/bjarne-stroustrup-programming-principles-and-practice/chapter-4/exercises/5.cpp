// Write a simple calculator, that can handle two doubles and an operand.
//
// e.g.
//
// 1 5 + => cout << "The sum of 1 and 5 is 6"
// 6 2 * => cout << "The multiplication of 6 and 2 is 12"

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>

double calculate(double a, double b, char operand)
{
    switch(operand)
    {
    case '+':
        return a + b;
        break;
    case '-':
        return a - b;
        break;
    case '/':
        return a / b;
        break;
    case '*':
        return a * b;
        break;
    default:
        throw std::invalid_argument("Unknown operand");
        break;
    }
}

int main()
{
    char operand = '\0';
    double a = 0,
           b = 0;

    std::cout << "Enter two numbers and an operand, RPN-style. > ";
    std::cin >> a >> b >> operand;
    std::cout << '\n' << calculate(a, b, operand) << '\n';
}
