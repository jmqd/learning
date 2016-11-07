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

        // int x = 4;
        // double d = 5 / (x - 2);
        // if (d = 2 * x + 0.5)
        // {
        //     std::cout << "Success!\n";
        // }
        //
        // problem 1: single '=' instead of '=='
        // problem 2: d being assigned as int rather than double

        // corrected
        int x = 4;
        double d = 5.0 / (x - 2);
        if (d == x / 2 + 0.5)
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
