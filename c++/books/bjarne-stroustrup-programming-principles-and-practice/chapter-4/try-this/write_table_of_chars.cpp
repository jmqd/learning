#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>

int main()
{
    char letter = 'a';
    int letter_int = int{letter};
    while (letter_int < int{'z'} + 1)
    {
        std::cout << letter << '\t' << letter_int << '\n';
        ++letter;
        ++letter_int;
    }
}

