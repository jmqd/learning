
def print_staircase(n):
    for i in xrange(0, n):
        print ' ' * (n - i - 1) + ('#' * (i + 1))

def test():
    cases = [4, 6, 32]
    for case in cases:
        print
        print_staircase(case)

def main():
    test()

def hackerrank_hook():
    n = int(raw_input().strip())
    print_staircase(n)

if __name__ == '__main__':
    main()
