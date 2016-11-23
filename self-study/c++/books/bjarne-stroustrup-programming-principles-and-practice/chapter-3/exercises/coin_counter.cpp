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

std::string coin_asker(std::string coin_type)
{
    return "Enter the number of " + coin_type + " you have > ";
}

double coins_to_dollars(int pennies, int nickels, int dimes, int quarters,
        int half_dollars, int one_dollar_coins)
{
    double amount = 0.00;

    amount += pennies * 0.01;
    amount += nickels * 0.05;
    amount += dimes * 0.10;
    amount += quarters * 0.25;
    amount += half_dollars * 0.50;
    amount += one_dollar_coins;
    return amount;
}


int main()
{
    // initialization
    int pennies;
    int nickels;
    int dimes;
    int quarters;
    int half_dollars;
    int one_dollar_coins;

    // user inputs
    std::cout << coin_asker("pennies");
    std::cin >> pennies;
    std::cout << coin_asker("nickels");
    std::cin >> nickels;
    std::cout << coin_asker("dimes");
    std::cin >> dimes;
    std::cout << coin_asker("quarters");
    std::cin >> quarters;
    std::cout << coin_asker("half dollars");
    std::cin >> half_dollars;
    std::cout << coin_asker("one dollar coins");
    std::cin >> one_dollar_coins;

    // logic
    double result = coins_to_dollars(pennies, nickels, dimes, quarters,
            half_dollars, one_dollar_coins);

    std::cout << "You have $" << result << " in your piggy bank.";
}
