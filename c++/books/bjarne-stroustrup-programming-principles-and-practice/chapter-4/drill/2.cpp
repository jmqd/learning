#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>

int main()
{
    bool first_iter = true;
    double input = 0;
    double largest = 0;
    double smallest = 0;

    while (std::cin >> input)
    {
        if (input == '|')
        {
            break;
        }
        else
        {
            if (first_iter)
            {
                largest = input;
                smallest = input;
                first_iter = false;
            }


            if (input > largest)
            {
                largest = input;
                std::cout << "largest so far\n";
            }
            if (input < smallest)
            {
                smallest = input;
                std::cout << "smallest so far\n";
            }
        }
    }
}
