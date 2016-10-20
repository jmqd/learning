// There is an old story that the emperor wanted to thank the inventor
// of the game of chess and asked the inventor to name his reward.
// The inventor asked for one grain of rice of the first square,
// 2 for the second, 4 for the third, and so on, doubling for each
// of the 64 squares. That may sound modest, but there wasn't enough
// rice in the empire to satisfy the request! Write a program to calculate
// how many squares are required to give the inventor at least 1000 grains
// of rice, at least 1,000,000 grains, at least 1,000,000,000 grains.

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<regex>
#include<map>


int calc_square_worth(int square_num)
{
    // binary num
    int grains_of_rice = 0b1;

    // 2^n can be represented in binary as 1 with n trailing 0s.
    // 2^0 -> 1  ->  0b1
    // 2^1 -> 2  ->  0b10
    // 2^2 -> 4  ->  0b100
    // 2^3 -> 8  ->  0b1000
    // 2^4 -> 16 ->  0b10000
    // ...
    // 1. Incrementing n in the exponent term 2^n is equivalent to (2^n) * 2.
    // 2. Let k = a binary number whose leftmost digit is 1 and all others 0.
    // 3. Appending a 0 to k is equivalent to k - k + 2k.
    // 4. From 3, appending a 0 to k is equivalent to 2*k.
    // 5. Therefore: 2^(n) == 0b1 << n
    return grains_of_rice << (square_num - 1);
}

int calc_squares_required(int grains_desired)
{
    int i = 1;
    int grains = 0;
    while (grains < grains_desired)
    {
        grains += calc_square_worth(i);
        ++i;
    }
    return i - 1;
}

void render_answer(int grains_wanted, int squares_required)
{
    std::cout << "In order to get at least " << grains_wanted << " grains of "
        "rice, " << squares_required << " squares are required.\n";
}

int main()
{
    int grains_wanted = 0;
    int squares_required = 0;
    std::vector<int> cases_grains_wanted {1000, 1000000, 1000000000};

    for (int grains_wanted: cases_grains_wanted)
    {
        squares_required = calc_squares_required(grains_wanted);
        render_answer(grains_wanted, squares_required);
    }
}
