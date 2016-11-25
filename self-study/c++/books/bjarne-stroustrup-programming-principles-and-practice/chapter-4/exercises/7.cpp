// Modify the calculator from exercise 5 to accept (just) single-digit
// numbers written as either digits or spelled out.

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<regex>
#include<map>

double assert_num(std::string num)
{
    std::map<std::string, int> string_to_num = {
        {"zero", 0},
        {"one", 1},
        {"two", 2},
        {"three", 3},
        {"four", 4},
        {"five", 5},
        {"six", 6},
        {"seven", 7},
        {"eight", 8},
        {"nine", 9}
        };
    std::string pattern = "[0-9]{1,}";
    std::regex regexp = std::regex(pattern);
    if (!std::regex_match(num, regexp))
    {
        return (double) string_to_num[num];
    }
    else
    {
        return (double) std::stoi(num);
    }
}


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
    std::string str_a = "";
    std::string str_b = "";
    char operand = '\0';

    std::cout << "Enter a calculation > ";
    std::cin >> str_a >> str_b >> operand;

    double a = assert_num(str_a);
    double b = assert_num(str_b);
    double answer = calculate(a, b, operand);

    std::cout << "\nThe answer is > " << answer << '\n';
}
