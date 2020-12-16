# https://www.acmicpc.net/problem/1157

word = input()

dictionary = {}

for letter in word:
    ascii_code = ord(letter)

    if(ascii_code>=97): ascii_code = ascii_code - 97
    else: ascii_code = ascii_code - 65

    ascii_code_count = dictionary.get(ascii_code)

    if (ascii_code_count == None):
        dictionary[ascii_code] = 1
    else:
        dictionary[ascii_code] = ascii_code_count + 1

max_ascii_code = 0
max_count = 0

for key in dictionary:
    value = dictionary.get(key)
    if(max_count < value):
        max_count = value
        max_ascii_code = key

for key in dictionary:
    value = dictionary.get(key)
    if(max_count == value and key != max_ascii_code):
        print("?")
        exit()
print(chr(max_ascii_code + 65))



