
names = ['jordan']
values_to_names = {}

def assign_names_to_values(names)
    for name in names:
        name_value = 0
        for letter in name:
            letter_value = ord(letter) - 96
            name_value += letter_value
        if name_value not in values_to_names:

def answer(names):


answer(names)
