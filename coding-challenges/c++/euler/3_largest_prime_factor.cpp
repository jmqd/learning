// What is the largest prime factor of the number 600851475143?

#include<iostream> // for cout and cin type of stuff
#include<vector> // vector data structure -- full featured array
#include<algorithm> // algorithm is for std::max_element
#include<math.h> // math.h for fmod(), which is % for doubles

int main() 
{
    double input = 600851475143; // the initial number 
    std::cout << "Getting largest prime factor for " << input << '\n';
    std::vector<double> factors;
    double divisor = 2;

    while (input > 1) 
    {
        while (fmod(input, divisor) == 0) 
        { 
            factors.push_back(divisor);
            input /= divisor; // this is the mathy-crafty part.
        }
        ++divisor;
        if (divisor*divisor > input) 
        { // the largest prime factor of a number is the edge case --
            if (input  > 1) // it is a perfect square, and its sqrt is prime
            { 
                factors.push_back(input);
                break;
            }
        }
    }
    int largest_prime_factor = *max_element(factors.begin(), factors.end());
    std::cout << largest_prime_factor << '\n';
    return 0;
}
