# https://www.acmicpc.net/problem/15552

import sys

testCaseT = int(input())

for testCase in range(testCaseT):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(A+B)