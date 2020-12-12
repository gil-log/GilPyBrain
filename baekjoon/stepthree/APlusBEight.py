#https://www.acmicpc.net/problem/11022

testCaseT = int(input())

for testCase in range(1, testCaseT+1):

    A, B = map(int, input().split())

    print("Case #%d: %d + %d = %d" %(testCase, A, B, A+B))