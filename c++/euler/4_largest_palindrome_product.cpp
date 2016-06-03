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
#include <vector>
#include <algorithm>

using std::vector;
using std::max_element;
using std::cout;
using std::endl;

bool isPalindrome(int input);

int main()
{
    std::vector<int> palindromes; 
    for (int outer = 999; outer > 500; --outer)
    {
        bool check_next = true;
        for (int inner = 999; inner > 500 && check_next; --inner)
        {
            int product = inner * outer;
            if (isPalindrome(product) && std::find(palindromes.begin(), palindromes.end(), product) == palindromes.end())
            {
                palindromes.push_back(product);              
                check_next = false;
            }
        }
    }

    int answer = *std::max_element(palindromes.begin(), palindromes.end());
    cout << answer;
    return answer;
}

// ....................................................................................................................
// I thought about casting to string and reversing, but I thought surely there ought to be a more elegant solution.
// So I Googled... and came across this solution on stackexchange. Definitely seems more elegant to me.
// http://stackoverflow.com/a/199218/5875532
// ....................................................................................................................
bool isPalindrome(int input) {
    int rev = 0;
    int num = input;
    while (num > 0) 
    {
        int dig = num % 10;
        rev = rev * 10 + dig;
        num /= 10;
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
