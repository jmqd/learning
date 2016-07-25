# Teaching a friend how to code via Python, part 1: Fib seq.

terms = [0, 1]
up_to_n = 10
while len(terms) <= up_to_n:
    terms.append(terms[-1] + terms[-2])

# This is a comment.
# The \n character is a "newline character."
print("\nThis computes the sequences and stores it all" \
    + " in memory, then prints it out.")
print(terms)
print("\n")

# Moving on to a different approach for the problem:

print("This computes the instances of every given n in the sequence up to N,")
print("printing out the instances as it goes, storing no more than two")
print("variables in memory at any given time. (Ignoring i and up_to_n.)")

a = 0
b = 1
for i in range(up_to_n - 1):
    # this is fancy python assignment syntax. you will love this.
    a, b = b, (a + b)
    print(b)
