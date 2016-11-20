/*
 * The max difference problem, formalized on page 1, asks for the maximum
 * profit that can be made by buying and then selling a single share of a stock
 * over a given day range.
 *
 * Write a program that computes the maximum profit that can be made by buying
 * and selling a share at most twice. The second buy must be made after the
 * first sale.
 */


#include<iostream>
#include<vector>
#include<algorithm>


// At first, I'll assume that I can use O(n) additional storage.
// I will work to iterate on this solution later.

double find_max_profit(const std::vector<double>& prices)
{
    double min_seen = std::numeric_limits<double>::max(),
           max_profit = std::numeric_limits<double>::min();
    std::vector<double> max_profits_forwards(prices.size());

    // first, we iterate over the list forwards, enumerating the maximum
    // possible profit at any given day i, using the minimum price seen.
    for (int i = 0; i < prices.size(); ++i)
    {
        if (prices[i] - min_seen > max_profit)
        {
            max_profit = prices[i] - min_seen;
        }

        if (min_seen > prices[i])
        {
            min_seen = prices[i];
        }

        max_profits_forwards[i] = max_profit;
    }

    // next, we iterate over the list backward, enumerating the maximum
    // possible profit using the greatest price seen.
    double max_seen = std::numeric_limits<double>::min();
    std::vector<double> max_profits_backwards(prices.size());
    max_profit = std::numeric_limits<double>::min();

    for (int i = prices.size() - 1; i > 0; --i)
    {
        if (max_seen - prices[i] > max_profit)
        {
            max_profit = max_seen - prices[i];
        }

        if (prices[i] > max_seen)
        {
            max_seen = prices[i];
        }

        max_profits_backwards[i] = max_profit;
    }

    // Now, we iterate over the vectors that contain the maximum profits,
    // considering the combined cases:
    //      case 1: iterate from the beginning of the stock prices and
    //          determine maximum possible profit on day i as
    //          prices[i] - min_seen.
    //      case 2: iterate from the end of the stock prices and
    //          determine the maximum possible profit on day i as
    //          max_seen - prices[i].
    // By now constructing a vector of values popualted like so:
    // combined[i] = forward_iter[i - 1] + backward_iter[i],
    // we can construct the maximum possible profit on any given day i.
    //
    // From there, it is a trivial operation of finding the maximum element.
    std::vector<double> final_max_profits(prices.size());

    for (int i = 0; i < max_profits_forwards.size(); ++i)
    {
        final_max_profits[i] = ((i == 0) ? 0 : max_profits_forwards[i - 1]) +
            max_profits_backwards[i];
    }

    return *std::max_element(final_max_profits.begin(), final_max_profits.end());
}

void test()
{
    std::vector<double> prices = {5, 8, 1, 2, 4, 3, 10, 5};
    double max_profit = find_max_profit(prices);
    std::cout << '\n' << max_profit << '\n';
}

int main()
{
    test();
    return 0;
}
