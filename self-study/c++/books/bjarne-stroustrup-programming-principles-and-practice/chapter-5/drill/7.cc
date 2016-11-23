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

        // if (cond)
        // {
        //     std::cout << "Success!\n";
        // }
        // else
        // {
        //     std::cout << "Fail!\n";
        // }

        // problem: using var cond w/o definition
        
        // corrected
        bool cond = true;
        if (cond)
        {
            std::cout << "Success!\n";
        }
        else
        {
            std::cout << "Fail!\n";
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
