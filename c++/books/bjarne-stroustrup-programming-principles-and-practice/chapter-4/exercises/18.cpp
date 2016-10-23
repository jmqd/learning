// Write a program to solve quadratic equations.

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<regex>
#include<map>

std::vector<double> solve(double a, double b, double c)
{
    std::vector<double> answer(2, 0);
    answer[0] = (-(b) + std::sqrt(std::pow(b, 2) - 4 * a * c)) / 2 * a;
    answer[1] = (-(b) - std::sqrt(std::pow(b, 2) - 4 * a * c)) / 2 * a;
    return answer;
}

int main()
{
    double a = 0,
           b = 0,
           c = 0;
    std::vector<double> ans;

    std::cout << "Quadratic Equation Solver\n";
    std::cout << "===========================================================";

    std::cout << "\nEnter a > ";
    std::cin >> a;
    std::cout << "a is " << a;

    std::cout << "\nEnter b > ";
    std::cin >> b;
    std::cout << "b is " << b;

    std::cout << "\nEnter c > ";
    std::cin >> c;
    std::cout << "c is " << c;

    ans = solve(a, b, c);
    std::cout << "\nThe solutions are: " << ans[0] << ", " << ans[1] << '\n';
}
