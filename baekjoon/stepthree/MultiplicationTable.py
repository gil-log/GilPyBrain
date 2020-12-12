# https://www.acmicpc.net/problem/2739


number = int(input())

for multipleNumber in range(1, 10):
    printNum = int(number * multipleNumber)
    print(number, "*", multipleNumber, "=", printNum)
