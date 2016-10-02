#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>

constexpr double inch_to_cm = 2.54;
constexpr double m_to_cm = 100;
constexpr double ft_to_cm = 12 * inch_to_cm;


double get_cm(double amount, char unit)
{
    switch (unit)
    {
        case 'c':
            return amount;
            break;
        case 'i':
            return inch_to_cm * amount;
            break;
        case 'm':
            return amount * m_to_cm;
            break;
        case 'f':
            return amount * ft_to_cm;
            break;
        default:
            return 0.0;
    }
}

int main()
{
    bool first_iter = true;
    std::vector<std::string> seen;
    char unit = '\0';
    double amount = 0;
    double largest = 0;
    double smallest = 0;
    double total = 0.0;

    while (std::cin >> amount >> unit)
    {
        if (amount == '|')
        {
            break;
        }

        if (unit != 'm' && unit != 'f' && unit != 'i' && unit != 'c')
        {
            std::cout << "I don't recognize that unit. Please try again.\n";
            continue;
        }
        else
        {
            if (first_iter)
            {
                largest = get_cm(amount, unit);
                smallest = get_cm(amount, unit);
                first_iter = false;
            }


            if (get_cm(amount, unit) > largest)
            {
                largest = get_cm(amount, unit);
                std::cout << amount << ' ' <<  unit << " is largest so far\n";
            }
            if (get_cm(amount, unit) < smallest)
            {
                smallest = get_cm(amount, unit);
                std::cout << amount << ' ' << unit << " is smallest so far\n";
            }
            total += get_cm(amount, unit);
            seen.push_back(std::to_string(amount) + " " + unit);
        }
    }
    std::cout << "Total meters seen so far: " << total / 100 << '\n';
    std::cout << "here are all of the values that I've seen: \n";
    for (std::string i: seen)
    {
        std::cout << i << '\n'; 
    }

}
