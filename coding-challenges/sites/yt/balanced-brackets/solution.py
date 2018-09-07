'''
Write a function that takes a string containing various types of brackets ([],
(), {}) and returns whether the brackets in the string are balanced & correctly
nested.
'''

OPENERS_TO_CLOSERS_MAP = {
    '(': ')',
    '{': '}',
    '[': ']'
}

def is_balanced(input_string: str) -> bool:
    '''Only considering inputs containing the set of valid characters.'''
    stack = []

    if len(input_string) & 1:
        return False

    for c in input_string:
        if c in OPENERS_TO_CLOSERS_MAP:
            stack.append(c)
        elif not stack:
            return False
        else:
            opener = stack.pop()
            if OPENERS_TO_CLOSERS_MAP[opener] != c:
                return False
    if stack:
        return False
    else:
        return True

# trues
print(is_balanced('()()()()()'))
print(is_balanced('(((())))'))
print(is_balanced('([({([])})])'))
print(is_balanced(''))
print(is_balanced('()'))
print(is_balanced('[]'))
print(is_balanced('{}'))

# falses
print(is_balanced(')'))
print(is_balanced('('))
print(is_balanced('([)]'))
