// Code with something broken changed to be unbroken.

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>

int main()
{
    // begin scaffolding template

    try
    {
        // broken code here
        // std::vector<int> v(10);
        // v(5) = 7;
        // if (v(5) != 7)
        // {
        //     std::cout << "Success!\n";
        // }
        //
        // problem:
        //      1. accessing elements of vector with parens
        //      instead of with square brackets
        //      2. != vs ==

        std::vector<int> v(10);
        v[5] = 7;
        if (v[5] == 7)
        {
            std::cout << "Success!\n";
        }

        return 0;
    }

    catch (std::exception& e)
    {
        std::cerr << "error: " << e.what() << '\n';
        return 1;
    }

    catch(...)
    {
        std::cerr << "Oops: Unknown exception!\n";
        return 2;
    }
}
