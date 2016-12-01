'''
Problem:
    You are given N numbers. Store them and find the second largest number.

    The first line contains N. The second line contains an array A of N
    integers each separated by a space.

Solution:
    Use a heap. Heaps are made for such problems. Could solve this the old
    fashioned way, iterating through the `distinct_arr`, of course... but
    where's the fun in that?

Gotcha:
    Make a set of the array, because we're looking for the second largest
    number, not the value of the element in the array ranked 2nd.

Analysis:
    Runtime:
        O(n)
        ~ theta(3n + 2)
            - build_heap is a theta(n) time complexity algorithm (occurs once)
            - list, set are linear at worst (occurs once each)
            - max() of two elements is O(2)
'''
from __future__ import print_function
import random # for testing
import heapq

def solve(arr):
    # to remove duplicates. cast back to list to pass to heapq
    distinct_arr = list(set(arr))

    # undocumented method of heapq. could also invert values of arr
    # to negative and use the usual methods to achieve a max heap.
    heapq._heapify_max(distinct_arr)

    # nodes of a heap (indexed starting at 0) have the following properties:
    # left child = (2 * i) + 1
    # right child = (2 * i) + 2
    # the root node is 0
    # the root node is the max element.
    #
    # all this is to say, to return the 2nd most maximum element, we need
    # only find the max of the i=1 and i=2 values (the left and right children
    # of the root node).
    # So, let's do that.
    return max(distinct_arr[1:3])

def test():
    test_case = [random.randint(0, 100) for _ in range(20)]
    print("Testing solution... finding 2nd largest number in arr...")
    print("The test case list is: ", test_case)
    print("The solution is:", solve(test_case))

def hackerrank_solve():
    '''Cheeky and byte-conserving solution to submit to webapp...'''
    n = int(raw_input())
    arr = list(set(int(x) for x in raw_input().split()))
    heapq._heapify_max(arr)
    print(max(arr[1:3]))

def main():
    test()

if __name__ == '__main__':
    main()
