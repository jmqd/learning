# Only about median performance on leetcode, but it's highly readable.
# I considered a prime number or ordinal approach, but it just seemed
# like premature optimization.

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list)

        for candidate in strs:
            groups[''.join(sorted(candidate))].append(candidate)

        return list(groups.values())

def execute_example_case():
    example = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    print(s.groupAnagrams(example))
