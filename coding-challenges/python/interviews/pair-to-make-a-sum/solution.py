#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import logging
logging_format = '[%(asctime)-15s][%(name)s][%(levelname)s][%(message)s]'
logging.basicConfig(level = logging.INFO, format = logging_format)

'''
Given an array of integers A and an integer k, find a pair of elements
that sum together to form k.
'''

'''
Clarifying questions:
    1. Can I assume these will all be positive integers?
        If so: the algorithms can be made more efficient by
            skipping an integer if it is greater than k.
'''

def solve_first(arr, k):
    '''First attempt (brute force solution).

    Note:
        This solution performs len(arr) - i - 1 operations for each
        iteration of the for loop.

        Peeking at that, assuming an arr length of 6, looks like this:
            operations = 5 + 4 + 3 + 2 + 1
        For the first iteration (i == 0), it performs 5 comparisons --
        one for each other element in the array. For the second, it performs
        4 operations, etc.

        This can be generalized as the sum of the natural numbers from 1 to n.
        e.g. 1 + 2 + 3 + 4 + ... + n.

        This arithmetic sum can be expressed in the following form:
            n * (n + 1) / 2

        The expression n * (n + 1) / 2 is asymptotically bounded by n**2.
        Therefore, this algorithm is O(n**2).
    '''
    for i in xrange(0, len(arr)):
        # If integers can be assumed to be positive only:
        # if arr[i] >= k:
        #    continue

        for j in xrange(i + 1, len(arr)):
            if arr[j] + arr[i] == k:
                return i, j
    return None

def solve_second(arr, k):
    '''Now, assume the array is in ascending order.

    Note:
        This solution is n·log(n) in the worst case, because binary search
        is a log(n) operation, and in the worst case, we must perform it upon
        all n elements of the input array.

        A more nuanced `theta` analysis would find the following:
            Θ(m·log(n)), where m = number of elements in arr < k
    '''

    # since we are now assuming that the array is sorted, it makes most
    # sense to search the arr[i..len(arr)] subarray via binary search
    def binary_search(arr, start, end, target):
        midpoint = (end + start) / 2
        if arr[midpoint] == target:
            logging.info('midpoint ({}) == target ({}); returning...'.format(
                midpoint, target))
            return midpoint
        elif end - start <= 1:
            return start if arr[start] == target else None
        elif arr[midpoint] > target:
            logging.info('midpoint too big; going to {}:{}'.format(start,
                midpoint + 1))
            return binary_search(arr, start, midpoint, target)
        elif arr[midpoint] < target:
            logging.info('midpoint too small; going to {}:{}'.format(
                midpoint, end))
            return binary_search(arr, midpoint, end, target)

    for i, elem in enumerate(arr):
        # If elem >= k, we know that we cannot find a matching integer in
        # the array to sum to k, because the array is in ascending order.
        # Additionally, we abort if we are on the last element, because
        # there are no more elements after the last, and a pair is needed.
        if elem >= k or i == len(arr) - 1:
            return None

        # using binary search, we search the remaining len(arr) - i
        # elements of the array for k - elem. We do this because there
        # is only one value which satisfies x + elem = k, and it is k - elem.
        match = binary_search(arr, i + 1, len(arr), k - elem)
        if match:
            return i, match
    return None

def solve_third(arr, k):
    '''Third iteration on the solution. There is an O(n) solution.

    Note:
        This solution exploits the fact that the list is sorted
        and simply makes two pointers, one at the end and one at the
        beginning, shrinking the windows of comparisons towards each
        other.

        It works because at any point, there is only one feasible operation
        to get closer to k: either increment i or decrement j. In this case,
        we keep our `band` of comparisons to only the range that might sum to k
    '''
    i, j = 0, len(arr) - 1
    while j > i:
        current_sum = arr[j] + arr[i]
        if current_sum == k: return i, j
        elif current_sum > k: j -= 1
        elif current_sum < k: i += 1
    return None

def solve_fourth(arr, k):
    '''Fourth iteration on the problem, using a hash table data structure.

    Note:
        For this solution, we are to assume that the array is not sorted.
        I will also assume that I can allocate O(n) additional memory.

        The runtime of this algorithm is O(n) and its space complexity is O(n)
    '''
    seen_complements = {}
    for i, elem in enumerate(arr):
        complement = k - elem
        if elem in seen_complements:
            return seen_complements[elem], i
        seen_complements[complement] = i
    return None

def test(arr, k, solution_func):
    print("Beginning test case...")
    print("arr\t= {arr}".format(arr = arr))
    print("k\t= {k}".format(k = k))
    print("Solution: ", solution_func(arr, k))

def main():
    # some test data
    test_arrs = [
            [5, 6, 1, 2, 5, 4, 3],
            [77, 12, 32, 64, 12, 3],
            [1, 1, 3, 7, 3, 5, 2],
            [1, 2, 5, 6, 7, 8, 9, 11, 15, 18, 23, 24],
            [1, 2, 4, 4]
        ]
    test_ks = [5, 43, 7, 38, 8]

    test(test_arrs[0], test_ks[0], solve_first)
    test(test_arrs[3], test_ks[3], solve_second)
    test(test_arrs[3], test_ks[3], solve_third)
    test(test_arrs[3], test_ks[2], solve_third)
    test(test_arrs[3], test_ks[2], solve_fourth)
    test(test_arrs[4], test_ks[4], solve_fourth)


if __name__ == '__main__':
    main()
