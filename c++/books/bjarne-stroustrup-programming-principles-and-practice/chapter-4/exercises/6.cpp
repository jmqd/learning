// Make a vector holding the ten string values "zero", "one", etc.
// Use that in a program that converts a digit to its corresponding
// spelled out value, and vice-a-versa.

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>

int main()
{
    // initializations
    char direction;
    std::vector<std::string> nums { "zero", "one", "two", "three", "four",
                                    "five", "six", "seven", "eight", "nine" };

    // controller
    std::cout << "Do you have a digit (d), or a spelled-out-value (s)? > ";
    std::cin >> direction;
    std::cout << "\nOkay, please enter the value to convert. > ";
    if (direction == 's')
    {
        std::string spelled_out_num = "";
        std::cin >> spelled_out_num;
        int digit = std::find(nums.begin(),
                nums.end(), spelled_out_num) - nums.begin();
        std::cout << '\n'
            << spelled_out_num
            << " corresponds to digit "
            << digit << '\n';
    }
    else if (direction == 'd')
    {
        int digit = 0;
        std::cin >> digit;
        std::string spelled_out_num = nums[digit];
        std::cout << '\n' << digit
            << " corresponds to spelled out name  '"
            << spelled_out_num << "'\n";
    }
    else
    {
        std::cout << "\nI don't understand that type of input.\n";
    }
}
