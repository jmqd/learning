# Think of an object in the following way:
#   An object is a set of keys and values. This set of keys and values composes
#       the "properties" of the object. This object also has functions that it
#       has special access to. These functions are called 'methods', solely
#       because they are associated with an object. But they're just functions.

# Before I go any further, I should explain what a dictionary is.

# To initialize your conception of a dictionary, think of a list.
# For example:

example_list = [1, 2, 3]

print("\nAccessing a list...\n")
# To access any given value of the list, we simply ask for the list's
# nth item, indexed from 0.
# E.g.

first_item = example_list[0]
second_item = example_list[1]

print(first_item)
print(second_item)
# In a dictionary, the 0 and 1 above would be specifically assigned indices.

# This is a dictionary.
dictionary = {'the first element': 'the first value', 'Ryan': 'Lestnor'}

print("\nAccessing a dictionary....\n")

# To access those elements looks like this:
first_item = dictionary['the first element']

name = 'Ryan' # simple variable assignment
nickname = dictionary[name] # using variable to lookup value in dictionary

print(first_item)
print(nickname)

# A few things to know:
#   A dictionary's keys are a set, i.e. you cannot have multiple keys with the
#       same name.
#   A dictionary has no guarentees about what order the items are in.
#       Bonus knowledge (advanced): A dictionary's implementation, under the
#           hood, is called a hash table. Hash tables are very important
#           structures in CS.

# Up next... more about objects.
