// Write a program that plays the game, 'Rock, Paper, Scissors'.
// Use a switch statement to solve this exercise. Also, the machine
// should give random answers. Real randomness is too hard to implement
// just now, so just build a vector with a sequence of values to be used
// as "the next value."

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<regex>
#include<map>
#include<chrono>
#include<thread>
#include<random>

void sleep(int seconds)
{
    std::this_thread::sleep_for(std::chrono::milliseconds(seconds * 1000));
}



void play_game()
{
    std::uniform_int_distribution<> dis(1,2);
    std::vector<std::string> choices = {"Rock", "Paper", "Scissors"};
    std::map<std::string, std::map<std::string, int>> result_matrix = {
        {"Rock", {{"Paper", false}, {"Scissors", true}}},
        {"Paper", {{"Rock", true}, {"Scissors", false}}},
        {"Scissors", {{"Paper", true}, {"Rock", false}}}
    };
    std::random_device rd;
    std::mt19937 mt(rd());
    std::string player_choice = "";
    std::string computer_choice = "";
    bool computer_wins = false;

    while (player_choice == computer_choice)
    {
        std::cout << "1..." <<'\n';
        sleep(1);
        std::cout << "2..." <<'\n';
        sleep(1);
        std::cout << "Enter your choice! (Rock, Paper, Scissors) > ";

        std::cin >> player_choice;
        computer_choice = choices[dis(mt)];
        computer_wins = result_matrix[computer_choice][player_choice];

        std::cout << "I chose " << computer_choice <<'\n';

        if (player_choice == computer_choice)
        {
            std::cout << "A draw! We have to go again...\n"; 
        }
    }
    
    if (computer_wins)
    {
        std::cout << "I win!\n";
        return;
    }
    std::cout << "You win. :(\n";
}

int main()
{
    char playing = '\0';

    std::cout << "\nReady to play? One-two-shoo, of course. (y/n) > ";
    std::cin >> playing;
    while (playing == 'y' || playing == 'Y')
    {
        play_game();
        std::cout << "Want to play again? (y/n) > ";
        std::cin >> playing;
    }
}
