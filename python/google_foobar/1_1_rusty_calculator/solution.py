def answer(str):
    mult = 0
    plus = 0
    new_str = ''
    for char in str:
        if char == '*':
            mult += 1
        if char == '+':
            plus += 1
            new_str += '*' * mult
            mult = 0
        if char != '*' and char != '+':
            new_str += char
    new_str += '+' * plus
    if mult > 0:
        new_str += mult * '*'
    return new_str

def tester():
    cases = [
        '2*4*3*2+1+2+3*1+3+1*0',
        '2+1',
        '2*2',
        ]
    for case in cases:
        print "Testing case: ", case
        print "Answer: ", answer(case)

tester()

