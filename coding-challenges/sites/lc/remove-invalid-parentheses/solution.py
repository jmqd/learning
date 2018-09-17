from collections import deque, Counter

PARENS = set('()')
GOLDEN_CASES = [
    (")(", [""]),
    ("(a)())()", ["(a)()()", "(a())()"]),
    ("()())()", ["()()()", "(())()"]),
    ("()(((((((()", ['()()'])
]

class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        valid_paren_strs = set()
        q = deque()
        q.appendleft(s)
        seen = set()
        while q:
            node = q.pop()
            if node in seen:
                continue
            else:
                seen.add(node)

            if is_valid(node):
                valid_paren_strs.add(node)

            if not valid_paren_strs:
                q.extendleft(neighbors(node))

        return list(valid_paren_strs)


def is_valid(s):
    openers = 0
    for index, c in enumerate(s):
        if c == '(':
            openers += 1
        elif c == ')':
            openers -= 1
            if openers < 0:
                return False
    return not openers


def neighbors(s):
    for i in range(len(s)):
        if s[i] in PARENS:
            yield s[:i] + s[i + 1:]


def test():
    s = Solution()
    for _in, expectation in GOLDEN_CASES:
        answer = s.removeInvalidParentheses(_in)
        print("Input is '{}' | Expecting {} | Got {}".format(_in, expectation, answer))
        assert Counter(expectation) == Counter(answer)

if __name__ == "__main__":
    test()
