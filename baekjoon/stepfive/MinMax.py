# https://www.acmicpc.net/problem/10818

integerNum = int(input())

listA = list(map(int, input().split()))

listA.sort()

print(listA[0], listA[integerNum-1])
