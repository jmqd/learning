class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for index, val in enumerate(nums):
            while nums[index] > 0 and nums[index] <= len(nums) and nums[index] != index + 1 and nums[index] != nums[nums[index] - 1]:
                nums[nums[index] - 1], nums[index] = nums[index], nums[nums[index] - 1]

        for index, i in enumerate(nums):
            if i != index + 1:
                return index + 1

        if nums:
            return index + 2
        else:
            return 1


def execute_example_cases():
    s = Solution()
    print(s.firstMissingPositive([1,2,0]))
    print(s.firstMissingPositive([3,4,-1,1]))
    print(s.firstMissingPositive([7,8,9,11,12]))
    print(s.firstMissingPositive([1]))
    print(s.firstMissingPositive([]))
    print(s.firstMissingPositive([2, 1]))

