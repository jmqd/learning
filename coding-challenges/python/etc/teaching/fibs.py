# Teaching a friend how to code via Python, part 1: Fib seq.
# A few observations:
#   - Notice none of my lines go beyond 80 characters. That is intentional.
#       It is a good practice that you should start immediately.
#   - Things "logically together" are together. A newline is put between
#       things that are categorically different somehow. It's kind of like
#       paragraps in essays.

# Initializing our variables.
terms = [0, 1]
up_to_n = 10

# len() is a function that returns an integer equal to the number of items
# in a list, set, dict, etc. This kinds of items are collectively called
# "collections," because they are collections of items (elements).

# the line below might be read as: "while the length of terms is less than or
# or equal to the variable up_to_n, do ..."

while len(terms) <= up_to_n:
    terms.append(terms[-1] + terms[-2])

# This is a comment.
# The \n character is a "newline character."
print("\nThis computes the sequences and stores it all" \
    + " in memory, then prints it out.")
print(terms)
print("\n")

# Moving on to a different approach for the problem:

print("This computes the instances of every given n in the sequence up to" \
    + " N, printing out the instances as it goes, storing no more than two" \
    + " variables in memory at any given time. (Ignoring i and up_to_n.)")

a = 0
b = 1
for i in range(up_to_n - 1):
    # this is fancy python assignment syntax. you will love this.
    a, b = b, (a + b)
    print(b)
