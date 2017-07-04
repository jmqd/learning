"""
Given two strings, write a method to
determine if one is a permutation of the other.
"""

string_1 = input("First string: ")
string_2 = input("Second string: ")

letter_counts = {}

def is_permutation(string_1, string_2):
    if len(string_1) != len(string_2):
        return False
    for letter in string_1:
        letter_counts[letter] = letter_counts.setdefault(letter, 0) + 1
    for letter in string_2:
        letter_counts[letter] = letter_counts[letter] - 1
    for key, value in letter_counts.items():
        if value != 0:
            return False
    return True

result = is_permutation(string_1, string_2)

if result:
    print("These strings are permutations of each other.")
if not result:
    print("These strings are not permutations of each other.")


