# https://www.acmicpc.net/problem/10950

testCaseT = int(input())

testCase = 1

while testCase <= testCaseT:
    testCase = testCase + 1
    A, B = map(int, input().split())
    print(A+B)
