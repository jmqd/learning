#include <iostream> // for cout and cin type of stuff
#include <vector> // vector data structure -- think of it like a more featured array
#include <algorithm> // algorithm for std::max_element, which retrieves max_element from a vector
#include <math.h> // math.h for fmod(), which is % for doubles

using std::vector; // boilerplate declarations
using std::cout;
using std::max_element;

int main() {
    double input = 600851475143; // the initial number for which we check its greatest prime factor
    std::vector <double> factors; // initialize the vector factors, which has elements of doubles
    double divisor = 2;

    while (input > 1) {
        while (fmod(input, divisor) == 0) { // if the divisor evenly divides the input value...
            factors.push_back(divisor); // append the divisor to the list
            input /= divisor; // set the input to the input / divisor. this is the crafty part.
        }
        ++divisor;
        if (divisor*divisor > input) { // the largest prime factor of a number is the edge case
            if (input  > 1) {          // where it is a perfect square, and its sqrt is prime
                factors.push_back(input);
                break;
            }
        }
    }
    int largest_prime_factor = *max_element(factors.begin(), factors.end());
    cout << largest_prime_factor;
    return largest_prime_factor;
}
