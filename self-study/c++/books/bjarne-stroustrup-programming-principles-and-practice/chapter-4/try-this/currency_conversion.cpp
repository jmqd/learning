// This file was constructed from a template designed for the first few
// chapters of the book to save time. It may be the case that some of these
// includes are unnecessary. That's okay.

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>

int main()
{
    char curr_type = '\0';
    double amount;
    constexpr double pounds_usd = 1.3;
    constexpr double yen_usd = 0.0099;
    constexpr double euro_usd = 1.12;
    double ratio = 0.0;
    double answer = 0.0;

    std::cout << "\nEnter the type of currency you have.\n\n"
        "pounds = p\nyen = y\neuros = e\n"
        "\n> ";
    std::cin >> curr_type;
    switch (curr_type)
    {
        case 'p':
            ratio = pounds_usd;
            break;
        case 'y':
            ratio = yen_usd;
            break;
        case 'e':
            ratio = euro_usd;
            break;
        default:
            std::cout << "I don't have knowledge of that currency.";
            return 0;
    }
    std::cout << "\nEnter the amount you have.\n> ";
    std::cin >> amount;
    answer = ratio * amount;
    std::cout << "In USD, " << amount << curr_type << " is $"
        << std::to_string(answer) << '\n';
}
