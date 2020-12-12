# https://www.acmicpc.net/problem/11021

testCaseT = int(input())

for testCase in range(1, testCaseT+1):
    A, B = map(int, input().split())
    print("Case #%d: %s" %(testCase, A+B))