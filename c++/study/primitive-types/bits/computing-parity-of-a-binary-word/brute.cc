// Implement a function that computes the parity of a binary word.
// (Parity of a binary word is determined by its occurences of bit == 1.)
//
// THIS IS THE BRUTE FORCE SOLUTION. Its time complexity is linear in time
// with respect to the length of the input binary word.
//
// O(n)

#include<iostream>
#include<string>

bool is_odd(int input)
{
    bool result = false;
    while (input)
    {
        result ^= (input & 1);
        input >>= 1;
    }
    return result;
}

int main()
{
    int input = 0;
    bool result = false;
    std::cin >> input;
    result = is_odd(input);
    std::cout << '\n' << input << " is "
        << ((result) ? "odd" : "even") << '\n';
}

