// ....................................
// Not currently working. Just testing
// isPalindrome() at the moment.
//
// TODO: 
//   - fix isPalindrome() ?
//   - find way to generate list of 
//       numbers to iterate through
//       isPalindrome().
// ....................................
#include <iostream>
using std::cout;

bool isPalindrome(int input);

int main()
{
   int number = 100;
   std::cout << isPalindrome(number);
   return isPalindrome(number);
}

// ....................................................................................................................
// I thought about casting to string and reversing, but I thought surely there ought to be a more elegant solution.
// So I Googled... and came across this solution on stackexchange. Definitely seems more elegant to me.
// http://stackoverflow.com/a/199218/5875532
// ....................................................................................................................
bool isPalindrome(int input) {
    int rev = 0;
    while (input > 0) 
    {
        int dig = input % 10;
        rev = rev * 10 + dig;
        input /= 10;
    }

    if (input == rev)
    {
        return true;
    }

    if (input != rev)
    {
        return false;
    }
}
