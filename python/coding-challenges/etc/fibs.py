# Teaching a friend how to code via Python, part 1: Fib seq.

terms = [0, 1]
up_to_n = 10
while len(terms) <= up_to_n:
    terms.append(terms[-1] + terms[-2])
# This is a comment.
# The \n character is a "newline character."
print("\nThis computes the sequences and stores it all in memory, then prints it out.")
print(terms)
print("\n\n")

a = 0
b = 1
print("This computes the instances of every given n in the sequence up to N, printing out the instances as it goes, storing no more than two variables in memory at any given time. (Ignoring i and up_to_n.)\n")
for i in range(up_to_n - 1):
   a, b = b, a + b
   print(b)
