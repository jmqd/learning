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
        // std::cout << "Success" << !\n"
        //
        // problem 1: No quotes wrapping !\n
        // problem 2: no semi-colon at EOL

        // corrected:
        std::cout << "Success" << "!\n";
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
