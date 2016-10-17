// Write a program to play a numbers guessing game.
// Program should be able to figure out the number I'm thinking of
// between 1 and 100 within 7 questions.

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>

bool prompt_participation()
{
    std::cout << "Would you like to play a game?... (y/n)\n";
    char opt_in = '\0';
    std::cin >> opt_in;

    if (opt_in == 'n' || opt_in == 'N')
    {
        return false;
    }

    if (opt_in == 'y' || opt_in == 'Y')
    {
        return true;
    }

    else
    {
        return prompt_participation();
    }
}

int guess(int prev_guess, int min = 0, int max = 100, char hint = 'i')
{
    if (hint == 'i')
    {
        return 50;
    }
    
    if (hint == 'h')
    {
        return (prev_guess - min) / 2 + min;
    }

    if (hint == 'l')
    {
        return (max - prev_guess) / 2 + prev_guess;
    }

    return 0;
}

int main()
{
    bool wants_to_play = prompt_participation();
    if (!wants_to_play)
    {
        std::cout << "Bye~";
        return 0; 
    }

    std::cout << "Think of a number between 1 and 100...\n";
    std::cout << "Let me know when you're ready to play by hitting enter...\n";
    std::string tmp = "";
    std::getline(std::cin, tmp);
    std::getline(std::cin, tmp);
    
    int num = 100;
    int max = 100;
    int min = 1;
    char hint = 'i';
    while (hint != 'c')
    {
        num = guess(num, min, max, hint);
        std::cout << "Is your number " << num << '\n'; 
        std::cout << "Enter c for correct, l for low, h for high.\n";
        std::cin >> hint;

        if (hint == 'l')
        {
            min = num;
        }
        else if (hint == 'h')
        {
            max = num;
        }   
    }
}

