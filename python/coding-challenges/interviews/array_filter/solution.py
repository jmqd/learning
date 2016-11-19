def functional_style(k, nums):
    print "Solving in \"functional\" style..."
    nums_filtered = list(filter(lambda x: x != k, nums))
    return nums_filtered + [k for i in range(0, len(nums) - len(nums_filtered))]

def imperative_style(k, nums):
    print "Solving in \"imperative\" style..."
    i = 0
    correct_length = len(nums)
    while i < correct_length:
        try:
            if nums[i] == k:
                del nums[i]
                i -= 1
        except IndexError:
            nums.append(k)
        i += 1
    return nums

def test():
    arr = [3, 2, 5, 2, 8, 2, 2, 13, 2, 21, 2, 34, 2]
    print functional_style(2, arr)
    print imperative_style(2, arr)

def main():
    test()

if __name__ == '__main__':
    main()
