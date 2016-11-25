// First program ran.
// Originally written at Cambridge University on May 6th, 1949

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>

int square(int i)
{
    return i * i;
}

int main()
{
    for (int i = 0; i < 100; ++i)
    {
        std::cout << '\t' << i << '\t' << square(i) << '\n';
    }
}

