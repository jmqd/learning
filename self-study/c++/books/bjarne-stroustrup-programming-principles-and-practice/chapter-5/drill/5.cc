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

        // std::string res = 5;
        // std::vector<int> v(10);
        // v[5] = res;
        // std::cout << "Success!\n";
        //
        // Problem: initialized 5 as std::string -- not int

        int res = 5;
        std::vector<int> v(10);
        v[5] = res;
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
