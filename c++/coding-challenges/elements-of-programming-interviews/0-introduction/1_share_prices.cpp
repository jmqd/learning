// Design an algorithm that determines the maximum profit that could have been
// made by buying and then selling a single share over a given day range,
// subject to the constraint that the buy and the sell have to take place
// at the start of the day. (You are given a list of days and the corresponding
// starting price of the stock.) (This algorithm may be needed to backtest a
// trading strategy.)

// just including boilerplate stuff. make no bones of these includes, please.
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>

int main()
{
    double min_seen = std::numeric_limits<double>::max();
    double max_profit = std::numeric_limits<double>::min();
    std::vector<double> opening_prices = {5, 8, 1, 2, 5};

    for (double i: opening_prices)
    {
        if (i - min_seen > max_profit)
        {
            max_profit = i - min_seen;
        }

        if (min_seen > i)
        {
            min_seen = i;
        }
    }
    std::cout << '\n' << max_profit;
}
