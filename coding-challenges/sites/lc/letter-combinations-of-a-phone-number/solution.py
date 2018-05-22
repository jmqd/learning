import itertools
import functools

KEYPAD = [
    "abc",
    "def",
    "ghi",
    "jkl",
    "mno",
    "pqrs",
    "tuv",
    "wxyz"
]

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        if len(digits) == 1:
            return list(KEYPAD[int(digits[0]) - 2])

        alpha_groups = [KEYPAD[int(x) - 2] for x in digits]
        return list(''.join(x) for x in itertools.product(*alpha_groups))

def main():
    solution = Solution()
    data = [
        {'in': "23", "out": ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]}
    ]
    for d in data:
        print("testing {in}, expecting {out}".format(**d))
        answer = solution.letterCombinations(d['in'])
        print("got {}".format(answer))
        assert answer == d['out']

if __name__ == '__main__':
    main()
