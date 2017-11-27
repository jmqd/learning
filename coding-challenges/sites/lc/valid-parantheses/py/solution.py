OPENERS = {'(', '{', '['}
CLOSER_MAP = {')': '(', '}': '{', ']': '['}

def solve(s: str) -> bool:
    stack = []
    for c in s:
        if c in OPENERS:
            stack.append(c)
        elif len(stack) == 0 or stack.pop() != CLOSER_MAP[c]:
            return False
    return True if len(stack) == 0 else False

def main() -> None:
    cases = [('()', True), ('([{}])', True), ('((([[)]))', False), ("([)]", False)]
    for case in cases:
        print("{} resulted in {}. Expected: {}".format(case, solve(case[0]), case[1]))

if __name__ == '__main__':
    main()

