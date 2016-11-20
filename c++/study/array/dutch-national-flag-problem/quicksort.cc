/*
 * Author: Jordan McQueen
 * Exploring the quicksort algorithm implementation.
 */

#include<vector>
#include<iostream>

void quicksort(std::vector<int>& v, int begin, int end)
{
    if ((end - begin) <= 0)
    {
        return;
    }
    int pivot = begin;
    for (int i = begin; i < end; ++i)
    {
        if (v[i] < v[end])
        {
            std::swap(v[i], v[pivot]);
            ++pivot;
        }
    }
    std::swap(v[pivot], v[end]);
    quicksort(v, begin, pivot - 1);
    quicksort(v, pivot + 1, end);
}

void test()
{
    std::vector<int> test_vector = {1, 4, 5, 7, 0, 6, 2, 8, 9, 3, 10, 11, 12, 13, 14, 15};
    quicksort(test_vector, 0, test_vector.size() - 1);
    for (int i: test_vector)
    {
        std::cout << '\n' << i;
    }
    std::cout << '\n';
}

int main()
{
    test();
    return 0;
}
