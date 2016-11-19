// Implement a function that computes the parity of a binary word.
// (Parity of a binary word is determined by its occurences of bit == 1.)
//
// This is better than the brute-force algorithm. It is better in the best
// and average cases, because it erases the lowest set bit in each iteration.
// In effect, its runtime is O(m), where m is the number of set bits.

#include<iostream>
#include<string>

bool is_odd(int input)
{
    bool result = false;
    while (input)
    {
        result ^= 1;
        input &= (input - 1);
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

