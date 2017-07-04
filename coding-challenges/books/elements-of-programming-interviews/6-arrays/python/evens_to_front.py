'''
Given an array A of integers, reorder its entries so that the even
integers appear first. Solve it without allocating addition storage.
'''
def is_even(num):
    return num % 2 == 0

def reorder(nums):
    next_even = 0
    for i in xrange(len(nums)):
        if is_even(nums[i]):
            nums[i], nums[next_even] = nums[next_even], nums[i]
            next_even += 1

def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    reorder(nums)
    print nums

if __name__ == '__main__':
    main()


