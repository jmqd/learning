"""
By considering the terms in the Fibonacci sequence whose values
do not exceed four million, find the sum of the even-valued terms.
"""

past, present, result, future = 0, 0, 0, 1
while(present < 4000000):
    if present % 2 == 0:
        result += present
    past = present
    present, future = future, future + present
print(result)

