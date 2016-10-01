// Odd or even exercise

#include<iostream>
#include<string>
#include<array>
#include<vector>
#include<algorithm>
#include<cmath>
inline void keep_open() {char ch; std::cin >> ch;}

int main()
{
    int a = 0;
    std::cout << "Enter an integer.\nLet a = ";
    std::cin >> a;
    std::cout << a << " is " << ((a % 2 == 0) ? "even" : "odd");
}
