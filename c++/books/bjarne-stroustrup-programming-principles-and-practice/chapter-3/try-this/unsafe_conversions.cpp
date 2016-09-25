// This file was constructed from a template designed for the first few
// chapters of the book to save time. It may be the case that some of these
// includes are unnecessary. That's okay.

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>

int main()  // C++ programs start by executing the main function
{
    double d = 0;
    while (std::cin >> d) {
        int i = d;  // try to squeeze a double into an int
        char c = i; // try to squeeze an int into a char
        int i2 = c; // get the integer value of the character
        std::cout << "d == " << d << '\n'   // the original double
             << "i == " << i << '\n'        // converted to int
             << "i2 == " << i2 << '\n'      // int value of char
             << "char(" << c << ")\n";      // the char
    }
}
