# https://www.acmicpc.net/problem/3052

listA = list()

for i in range(10):
    number = int(input())
    listA.append(number % 42)

setA = set(listA)

print(len(setA))
