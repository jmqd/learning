class Solution:
    def searchInsert(self, nums, target):
        """
        Given a sorted array and a target value, return the index if the target
        is found. If not, return the index where it would be if it were
        inserted in order. You may assume no duplicates in the array.
        """
        return binary_search(nums, target, 0, len(nums) - 1)

def binary_search(nums, target, low, hi):
    print("low", low, "high", hi)
    candidate = nums[midpoint(low, hi)]

    if abs(hi - low) <= 1:
        if nums[low] > target:
            return low
        elif nums[hi] > target:
            return midpoint(low, hi)
        elif nums[hi] < target:
            return hi + 1
        else:
            return midpoint(low, hi) + 1

    if candidate == target:
        return midpoint(low, hi)
    elif candidate < target:
        return binary_search(nums, target, midpoint(low, hi), hi)
    elif candidate > target:
        return binary_search(nums, target, low, midpoint(low, hi))

def midpoint(low, hi):
    return (low + hi) / 2

