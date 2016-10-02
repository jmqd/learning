#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>

int main()
{
    int a = 0;
    int b = 0;
    std::vector<int> nums;

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
            if (nums[0] != nums[1])
            {
                for (int i = 0; i < nums.size(); ++i)
                {
                    std::string comp = (i == 0) ? "smaller" : "larger";
                    std::cout << nums[i] << " is the " << comp << " number\n"; 
                }
            }

            if (nums[0] == nums[1])
            {
                std::cout << "the numbers are equal.\n";
            }
        }
        nums.clear();
    }
}
