import sys

string = sys.argv[1]

def compress_string(string):
    compressed_string = string[0]
    count = 1
    previous_letter = string[0]

    for letter in string[1:]:
        if previous_letter == letter:
            count += 1

        if previous_letter != letter:
            if count > 2:
                compressed_string += str(count)
            elif count <= 2:
                compressed_string += previous_letter

            compressed_string += letter
            count = 1

        previous_letter = letter

    if count > 2:
        compressed_string += str(count)
    elif count <= 2:
        compressed_string += previous_letter

    return compressed_string

print(compress_string(string))
