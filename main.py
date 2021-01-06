name = "Name"
binary = ' '.join(format(ord(x), 'b') for x in name)

binary_values = binary.split()

ascii_string = ""
for binary_value in binary_values:
    an_integer = int(binary_value, 2)

    ascii_character = chr(an_integer)

    ascii_string += ascii_character

print(ascii_string)