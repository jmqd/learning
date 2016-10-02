#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>

int main()
{
    double a = 0;
    double b = 0;
    std::vector<double> nums;

    while (std::cin >> a >> b)
    {
        if (a == '|' || b == '|')
        {
            break;
        }
        else
        {
            // 2nd drill: larger and smaller
            nums.push_back(a);
            nums.push_back(b);
            std::sort(nums.begin(), nums.end());
            bool nums_equal = nums[0] == nums[1];

            if (nums_equal)
            {
                std::cout << "the numbers are equal.\n";
                nums.clear();
                continue;
            }

            for (int i = 0; i < nums.size(); ++i)
            {
                std::string comp = (i == 0) ? "smaller" : "larger";
                std::cout << nums[i] << " is the " << comp << " number\n"; 
            }

            double difference = nums[1] - nums[0];

            if (difference < 0.01)
            {
                std::cout << "the numbers are almost equal.\n";
            }
        }
        nums.clear();
    }
}
