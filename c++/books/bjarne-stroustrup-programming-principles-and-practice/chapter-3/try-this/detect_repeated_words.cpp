// This file was constructed from a template designed for the first few
// chapters of the book to save time. It may be the case that some of these
// includes are unnecessary. That's okay.

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
inline void keep_open() {char ch; std::cin >> ch;}

int main()  // C++ programs start by executing the main function
{
    std::string previous = " "; // previous word; initialized to "not a word"
    std::string current;
    int word_index = 0;
    while (std::cin >> current) {
        if (previous == current) {
            std::cout << "at word index " << word_index << ":\n";
            std::cout << "repeated word: " << current << "\n";
        }
        ++word_index;
        previous = current;
    }
}

