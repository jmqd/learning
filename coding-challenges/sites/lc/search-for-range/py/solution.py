from typing import List
from typing import Optional

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]

        return solve(target, nums, 0, len(nums) - 1)

def solve(
        target: int,
        vals: List[int],
        start: int,
        end: int) -> Optional[List[int]]:
    mid = get_mid(start, end)

    if start > end:
        return [-1, -1]
    elif vals[mid] == target:
        lower = binary_search_lower_bound(target, vals, 0, mid)
        upper = binary_search_upper_bound(target, vals, mid, len(vals) - 1)
        return [lower, upper]
    elif start == end:
        return [-1, -1]
    elif vals[mid] > target:
        return solve(target, vals, start, mid - 1)
    elif vals[mid] < target:
        return solve(target, vals, mid + 1, end)

def binary_search_lower_bound(
        target: int,
        vals: List[int],
        start: int,
        end: int) -> int:
    mid = get_mid(start, end)
    if vals[mid] != target:
        return binary_search_lower_bound(target, vals, mid + 1, end)
    elif mid == 0:
        return 0
    elif vals[mid - 1] != target:
        return mid
    else:
        return binary_search_lower_bound(target, vals, start, mid - 1)


def binary_search_upper_bound(
        target: int,
        vals: List[int],
        start: int,
        end: int) -> int:
    mid = get_mid(start, end)
    if vals[mid] != target:
        return binary_search_upper_bound(target, vals, start, mid)
    elif mid == len(vals) - 1:
        return mid
    elif vals[mid + 1] != target:
        return mid
    else:
        return binary_search_upper_bound(target, vals, mid + 1, end)


def get_mid(start: int, end: int) -> int:
    return start + (end - start) // 2

def not_in_array_case() -> None:
    arr = [2, 2]
    target = 1
    expected = [-1, -1]
    run_test_case(arr, target, expected)

def array_all_same_case() -> None:
    arr = [2, 2]
    target = 2
    expected = [0, 1]
    run_test_case(arr, target, expected)

def run_test_case(arr: List[int], target: int, expected: List[int]) -> None:
    solution = solve(target, arr, 0, len(arr) - 1)
    passing = solution == expected
    print("FAIL:" if not passing else "PASS:", arr, "with target of", target, "testcase evaluated to", solution)

def main() -> None:
    not_in_array_case()
    array_all_same_case()

if __name__ == '__main__':
    main()

