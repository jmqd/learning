# This is the solution to the problem if the lines would "partition"
# the containers, as physics works in real life.
# This particular problem doesn't care about partitioning the water, though.

HEIGHT = 0
INDEX = 1
BOUNDING_HEIGHT = 2
class Solution:
    '''
    Given n non-negative integers a1, a2, ..., an, where each represents a
    point at coordinate (i, ai). n vertical lines are drawn such that the two
    endpoints of line i is at (i, ai) and (i, 0). Find two lines, which
    together with x-axis forms a container, such that the container contains
    the most water.

    Note: You may not slant the container and n is at least 2.
    '''
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_volume = 0
        most_voluminous_container = (-1, -1)
        container = [0, 0, 0]

        for index, h in enumerate(height):
            if h >= container[HEIGHT] or h > container[BOUNDING_HEIGHT]:
                if h >= container[HEIGHT]:
                    volume = (index - container[INDEX]) * min(h, container[HEIGHT])
                else:
                    container[BOUNDING_HEIGHT] = h
                    volume = (index - container[INDEX]) * h

                if volume > max_volume:
                    max_volume = volume
                    most_voluminous_container = (container[INDEX], index)

                if h >= container[HEIGHT]:
                    container = [h, index, 0]
        return max_volume

def test():
    data = [
        {'in': [3, 0, 0, 3], 'out': 9},
        {'in': [3, 0, 0, 1], 'out': 3},
        {'in': [0, 0, 0, 1], 'out': 0},
        {'in': [0, 0, 0, 1, 1], 'out': 1},
        {'in': [1, 6, 1, 1, 3], 'out': 9},
    ]

    solution = Solution()
    for d in data:
        ans = solution.maxArea(d['in'])
        print("max_volume in {} should be {}. answer: {}".format(d['in'], d['out'], ans))

if __name__ == "__main__":
    test()
