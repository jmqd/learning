class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'

        num = 1

        for _ in range(n - 1):
            stack = []
            stack.append({'n': 1, 'c': num % 10})
            num //= 10

            while num:
                char = num % 10
                num //= 10

                if stack[-1]['c'] == char:
                    stack[-1]['n'] += 1
                else:
                    stack.append({'n': 1, 'c': char})

            mult = 1
            for grp in stack:
                num += mult * grp['c']
                mult *= 10
                num += mult * grp['n']
                mult *= 10

        phrase = str(num)
        return phrase

def main():
    data = [
        {'in': 1, 'out': '1'},
        {'in': 4, 'out': "1211"}
    ]
    s = Solution()
    for d in data:
        ans = s.countAndSay(d['in'])
        print(ans)
        assert ans == d['out']

if __name__ == '__main__':
    main()
