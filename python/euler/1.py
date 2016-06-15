"""
Find the sum of all the multiples of 3 or 5 below 1000.
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n")
args = parser.parse_args()

end_of_range = int(args.n)
sum = 0
for integer in range(end_of_range):
    if integer % 3 == 0 or integer % 5 == 0:
        sum += integer
print(sum)
