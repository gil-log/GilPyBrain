# https://www.acmicpc.net/problem/5622

word = input()

time = 0
for letter in word:
    if(letter == 'A' or letter == 'B' or letter == 'C'):
        time = time + 3

    elif(letter == 'D' or letter == 'E' or letter == 'F'):
        time = time + 4
    elif(letter == 'G' or letter == 'H' or letter == 'I'):
        time = time + 5

    elif(letter == 'J' or letter == 'K' or letter == 'L'):
        time = time + 6
    elif(letter == 'M' or letter == 'N' or letter == 'O'):
        time = time + 7

    elif (letter == 'P' or letter == 'Q' or letter == 'R' or letter == 'S'):
        time = time + 8

    elif (letter == 'T' or letter == 'U' or letter == 'V'):
        time = time + 9

    elif (letter == 'X' or letter == 'Y' or letter == 'W' or letter == 'Z'):
        time = time + 10

print(time)