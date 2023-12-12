
with open('sample.txt', 'r') as file:
    matrix_text = []
    for line in file.readlines():
        matrix_text.append(line.splitlines()[0])
# print(matrix_text)

import re

decoded_string = ""
j = 0
while len(matrix_text) > 0:
    try:
        i = 0
        for string in matrix_text:
            decoded_string += string[j]
            i += 1
        print(matrix_text)
        print(decoded_string)
        j += 1
    except IndexError:
        print(i)
        matrix_text.pop(i)
        print(matrix_text)

print(decoded_string)
regex = re.findall("(?<=[a-zA-Z1-9])[#|$|%|!|\s]{2,}(?=[a-zA-Z1-9])", r"{:s}".format(decoded_string))
print(regex)
for i in regex:
    decoded_string = decoded_string.replace(i, " ")

print(decoded_string)

