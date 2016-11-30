def hackerrank_solve():
    n, m = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    a, b = (set(int(x) for x in raw_input().split()) for _ in range(2))
    happiness = 0
    for i in arr:
	if i in a: happiness += 1
	if i in b: happiness -= 1
    print happiness

def main():
    hackerrank_solve()
    return 0

if __name__ == '__main__':
    main()
