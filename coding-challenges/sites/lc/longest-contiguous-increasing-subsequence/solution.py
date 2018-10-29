'''
https://leetcode.com/problems/longest-continuous-increasing-subsequence/

Beats > 90% of python3 solutions.
'''
def solve(arr):
    if len(arr) < 2:
        return len(arr)

    current_run = 1
    longest_run = 1

    for i in range(1, len(arr)):
        if arr[i - 1] < arr[i]:
            current_run += 1
        else:
            current_run = 1

        if current_run > longest_run:
            longest_run = current_run

    return longest_run

def main():
    data = [100, -1, 2, 5, 7, 100, -5, 10, -1]
    print("length of longest contiguously increasing subseq of {} is {}".format(data, solve(data)))

if __name__ == "__main__":
    main()
