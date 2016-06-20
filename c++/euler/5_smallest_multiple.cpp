// This doesn't compile. Something is badly wrong with this.
//
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


int main()
{
    std::vector<int> primeFactorization(int current);
    int begin = 1;
    int end = 10;
    std::map<int, int> prime_factorization;


    for (int current = begin; current <= end; ++current)
    {
        std::vector<int> prime_factors = primeFactorization(current);

        for (auto kv : prime_factorization)
        {
            int count = std::count_if(prime_factors.begin(), 
                                      prime_factors.end(),
                                      [prime_factorization, kv](int i) 
            {
                return i == prime_factorization.find(kv.first).first; 
            }
            );
            if (count > kv.second)
            {
                prime_factorization[kv.first] = count;
            }
        }
    }

    for (auto& elem : prime_factorization)
    {
        std::cout << elem.first << " " << elem.second << "\n";
    }
}

std::vector<int> primeFactorization(int num)
{
	std::vector<int> values;
	while (num % 2 == 0)
    {
		values.push_back(2);
        num /= 2;
    }
 
    for (int divisor = 3; divisor * divisor <= num; divisor += 2)
    {
        while (num % divisor == 0)
        {
            values.push_back(divisor);
            num /= divisor;
        }
    }
 
    // This condition is to handle the case whien n is a prime number
    // greater than 2
    if (num > 2)
	{
		values.push_back(num);
	}
	return values;
}
