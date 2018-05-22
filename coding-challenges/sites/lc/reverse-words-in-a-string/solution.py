class Solution(object):
    def reverseWords(self, s):
        return ' '.join(s.strip().split()[::-1])

def main():
    solution = Solution()
    data = [
        {'in': 'a few words', 'out': 'words few a'},
        {'in': ' a few words', 'out': 'words few a'},
        {'in': ' a few  words', 'out': 'words few a'},
    ]
    for d in data:
        print "testing sentence {in}, expecting {out}".format(**d)
        assert solution.reverseWords(d['in']) == d['out']

if __name__ == "__main__":
    main()
