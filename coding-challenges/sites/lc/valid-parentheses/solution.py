OPENERS = {'[': ']', '(':')', '{': '}'}
CLOSERS = {v: k for k, v in OPENERS.items()}

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i in OPENERS:
                stack.append(i)
            elif i in CLOSERS:
                try:
                    if CLOSERS[i] != stack.pop(): return False
                except:
                    return False
        return not stack


