# https://www.acmicpc.net/problem/1110

number = int(input())

oldNumber = number

count = 0

newNumber = -1


if(number <= 9 and number>0):
    number = number * 10 + number
    count = count + 1

if(number == 0):
    print(1)

else:
    while True:
        units = number % 10
        tens = int((number - units) / 10)
        newNumber = (units * 10) + (tens + units) % 10
        count = count + 1
        if(oldNumber == newNumber):
            break
        number = newNumber
    print(count)