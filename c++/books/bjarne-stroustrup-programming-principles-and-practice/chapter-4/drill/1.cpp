#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>

int main()
{
    int a = 0;
    int b = 0;
    while (std::cin >> a >> b)
    {
        if (a == '|' || b == '|')
        {
            break;
        }
        else
        {
            std::cout << a << b;
        }
    }
}
