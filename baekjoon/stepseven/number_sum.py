# https://www.acmicpc.net/problem/11720

count = int(input())

numbers = input()

sum = 0

for i in range(count):
    units = int(numbers[i])
    sum = sum + units
print(sum)