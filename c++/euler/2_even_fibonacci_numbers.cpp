#include <iostream>
using std::cout;
using std::endl;

int main() {
    // initialize the fib sequence...
    int latest, tmp, sum, middle, low;
    tmp = 0;
    low = 0;
    middle = 0;
    latest = 1;
    sum = latest; // initialize the sum at 1. a bit hacky...

    while (true) {
        tmp = latest;
        latest += middle;
        low = middle;
        middle = tmp;
        if (latest > 4000000) {
            break;
        }
        if (latest & 1) {
            sum += latest;
        }
    }
    std::cout << sum;
    return sum;
}
