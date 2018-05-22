import re
matcher = re.compile(r'^ *([-\+]?\d+)')

class Solution:
    def myAtoi(self, str):
        '''
        Using the stupid stub that the site provided, overriding `str`.
        '''
        match = matcher.match(str)

        if not match:
            return 0

        else:
            num = int(match.group(1))
            if num > 0:
                return min(num, 2**31 - 1)
            elif num < 0:
                return max(num, -2**31)
            else:
                return 0

def main():
    data = [
        {'in': '32', 'out': 32},
        {'in': '-32', 'out': -32},
        {'in': '+42', 'out': 42},
        {'in': ' 41', 'out': 41},
        {'in': '313 13', 'out': 313},
        {'in': ' 23 41', 'out': 23},
        {'in': '-999999999999', 'out': -2**31},
        {'in': '999999999999', 'out': 2**31 - 1},
        {'in': '0', 'out': 0},
    ]

    solution = Solution()
    for d in data:
        print("testing {in}; expecting {out}".format(**d))
        assert solution.myAtoi(d['in']) == d['out']

if __name__ == '__main__':
    main()
