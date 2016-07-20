"""
1. Implement an algorithm to determine if a string has all unique characters.
2. What if you cannot use additional data structures?
"""
import time

# 1.

string = input('Enter string: ')
already_checked = []

def is_unique(string):
    for letter in string:
        if letter in already_checked:
            return False
        already_checked.append(letter)
    return True

start = time.clock() # to time it...
string_is_unique = is_unique(string)
end = time.clock()

list_time = end - start

if string_is_unique:
    print("String is unique.")
if not string_is_unique:
    print("String is not unique.")
print("Using list data structure took ", list_time, " seconds")

# 2. If I cannot use additional data structures:

def brutish_is_unique(string):
    for letter in string:
        next_letter_index = string.index(letter) + 1
        for any_other_letter in string[next_letter_index:]:
            if letter == any_other_letter:
                return False
    return True

start = time.clock() # to time it...
string_is_unique = brutish_is_unique(string)
end = time.clock()

brute_time = end - start

if string_is_unique:
    print("String is unique.")
if not string_is_unique:
    print("String is not unique.")
print("Using no additional data structure took ", brute_time, " seconds")




