// Write a program that is a naive letter generator.
//
// TODO:
//  - make it to accept whole line of input.

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
inline void keep_open() {char ch; std::cin >> ch;}

int main()
{
    // initializations
    std::string name = "";
    std::string last_seen = "";
    std::string activity = "";
    std::string mutual_friend = "";
    char friend_sex = '0';
    int friend_age = 0;
    std::string author_name = "";

    // user input
    std::cout << "Recepient name: ";
    std::cin >> name;
    std::cout << "When did you last see them? ";
    std::cin >> last_seen;
    std::cout << "Beginning with a verb, desribe an"
        "activity you'd like to suggest: ";
    std::cin >> activity;
    std::cout << "Who is a mutual friend? > ";
    std::cin >> mutual_friend;
    std::cout << mutual_friend << " is 'M' or 'F'?";
    std::cin >> friend_sex;
    std::cout << mutual_friend << " is how old (in years): ";
    std::cin >> friend_age;
    std::cout << "What is your name? ";
    std::cin >> author_name;

    // processing, if needed:
    std::string friend_pronoun = (friend_sex == 'M') ? "he" : "she";

    std::string letter_contents = "Dear " + name + ",\n\n"
        "It has been " + last_seen + " since I've seen you.\n"
        "I am looking forward to " + activity + " with you in the near future."
        "\nHave you seen " + mutual_friend + " lately? I hope"
        " " + friend_pronoun + " is doing well\n. I heard " + friend_pronoun +
        " is turning " + std::to_string(friend_age + 1) + " next year...\n\n\n"
        "In any event, yours truly,\n\n" + author_name;
    std::cout << letter_contents;
}
