# https://www.acmicpc.net/problem/1002

test_case = int(input())

for i in range(test_case):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = ((abs(x1 - x2) ** 2) + (abs(y1 - y2) ** 2)) ** 0.5

    big_r = r1
    small_r = r2

    if(r1 > r2):
        big_r = r1
        small_r = r2
    elif(r1 < r2):
        big_r = r2
        small_r = r1

    if(x1 == x2 and y1 == y2 and r1 == r2):
        print(-1)
        continue

    if(d == (r1 + r2) or d == big_r - small_r):
        print(1)
        continue

    if(d<(r1+r2) and d>(big_r - small_r)):
        print(2)
        continue

    if(d > (r1+r2) or d < big_r - small_r):
        print(0)
        continue

