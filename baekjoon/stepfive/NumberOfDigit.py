# https://www.acmicpc.net/problem/2577

digit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

A = int(input())
B = int(input())
C = int(input())

number = A * B * C

while number > 0:
    units = number % 10
    if units == 0 : digit[0] = digit[0] + 1
    elif units == 1 : digit[1] = digit[1] + 1
    elif units == 2 : digit[2] = digit[2] + 1
    elif units == 3 : digit[3] = digit[3] + 1
    elif units == 4 : digit[4] = digit[4] + 1
    elif units == 5 : digit[5] = digit[5] + 1
    elif units == 6 : digit[6] = digit[6] + 1
    elif units == 7 : digit[7] = digit[7] + 1
    elif units == 8 : digit[8] = digit[8] + 1
    elif units == 9 : digit[9] = digit[9] + 1
    number = int(number / 10)

for i in range(10):
    print(digit[i])