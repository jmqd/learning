"""
Implement a method to perform basic string compression using the
counts of repeated characters. For example, 'aaabbbbchhh' would become
'a3b4ch3'. If the compressed string would not be smaller than the
original string, your method should return the original string.
"""

string = input("String to be compressed: ")
new = []
compressed = False
i = 0
count = 0
while not compressed:
    if i == len(string) - 1:
        compressed = True
        break
    while string[i] == string[i + 1]:
        count = count + 1
        i = i + 1
    if count > 1:
        new.append(string[i])
        new.append(str(count + 1))
        count = 0
    else:
        new.append(string[i - count:i + 1])
    i = i + 1
    if i == len(string) - 1:
        new.append(string[i])
        compressed = True
compressed_string = ''.join(new)

if len(compressed_string) < len(string):
    print(compressed_string)
else:
    print(string)


