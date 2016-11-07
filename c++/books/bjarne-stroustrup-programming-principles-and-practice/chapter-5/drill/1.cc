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
        
        // std::Cout << "Success!\n";
        // 
        // problem: capital C in std::cout call

        // corrected version:
        std::cout << "Success!\n";

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
