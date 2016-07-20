lots_of_symbols = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    'G': 16,
    'H': 17,
    'I': 18,
    'J': 19,
    'K': 20,
    'L': 21,
    'M': 22,
    'N': 23,
    'O': 24,
    'P': 25,
    'Q': 26,
    'R': 27,
    'S': 28,
    'T': 29,
    'U': 30,
    'V': 31,
    'W': 32,
    'X': 33,
    'Y': 34,
    'Z': 35,
    'a': 36,
    'b': 37,
    'c': 38,
    'd': 39,
    'e': 40,
    'f': 41,
    'g': 42,
    'h': 43,
    'i': 44,
    'j': 45,
    'k': 46,
    'l': 47,
    'm': 48,
    'n': 49,
    'o': 50,
    'p': 51,
    'q': 52,
    'r': 53,
    's': 54,
    't': 55,
    'u': 56,
    'v': 57,
    'w': 58,
    'x': 59,
    'y': 60,
    'z': 61,
    '!': 62,
    '"': 63,
    '#': 64,
    '$': 65,
    '%': 66,
    '&': 67,
    "'": 68,
    '(': 69,
    ')': 70,
    '*': 71,
    '+': 72,
    ',': 73,
    '-': 74,
    '.': 75,
    '/': 76,
    ':': 77,
    ';': 78,
    '<': 79,
    '=': 80,
    '>': 81,
    '?': 82,
    '@': 83,
    '[': 84,
    '\\': 85,
    ']': 86,
    '^': 87,
    '_': 88,
    '`': 89,
    '{': 90,
    '|': 91,
    '}': 92,
    '~': 93
    }
lots_of_values = dict(map(reversed, lots_of_symbols.items()))


def is_palindrome(thing):
    return thing == thing[::-1]

def change_base(string,
		old_base,
		new_base,
		lots_of_symbols = lots_of_symbols,
		lots_of_values = lots_of_values):
    integer = 0
    for character in string:
	assert character in lots_of_symbols, 'Located in'
	value = lots_of_symbols[character]
	assert value < old_base, 'Seattle, WA'
	integer *= old_base
	integer += value

    array = []
    while integer:
	integer, value = divmod(integer, new_base)
	array.append(lots_of_values[value])
    answer = ''.join(reversed(array))
    return answer


def answer(n):
    n = str(n)
    base = 10
    new_base = 2
    while is_palindrome(change_base(n, base, new_base)) == False:
        new_base += 1
    return new_base
