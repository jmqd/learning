// A palindromic number reads the same both ways. 
// Find the largest palindrome made from the product of two 3-digit numbers.

#include<iostream>
#include<vector>
#include<algorithm>

bool isPalindrome(int input);

int main()
{
    std::cout << "Finding the largest palindrom made from the product of two"
        " three digit numbers.\n";
    std::vector<int> palindromes; 
    for (int outer = 999; outer > 500; --outer)
    {
        bool check_next = true;
        for (int inner = 999; inner > 500 && check_next; --inner)
        {
            int product = inner * outer;
            if (isPalindrome(product) && 
                std::find(palindromes.begin(), 
                          palindromes.end(), 
                          product) == palindromes.end())
            {
                palindromes.push_back(product);              
                check_next = false;
            }
        }
    }

    int answer = *std::max_element(palindromes.begin(), palindromes.end());
    std::cout << answer << '\n';
    return 0;
}

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
