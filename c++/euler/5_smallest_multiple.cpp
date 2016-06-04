// What is the smallest positive number that is evenly 
// divisible by all of the numbers from 1 to 20?

#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using std::map;
using std::cout;
using std::endl;
using std::vector;

int isPrime();

int main()
{
    int begin = 1;
    int end = 10;
    std::vector<int> prime_factors;

    for (int i = begin; i <= end; ++i)
    {
        prime_factors.push_back(i);
    }
}

int isPrime(int num)
{
   for (int i = 1; i < num, ++i)
   {
        if (i % num == 0)
        {
            return false;
        }
   }
   return true;
}
