# https://www.acmicpc.net/problem/3009

one_x, one_y = map(int, input().split())
two_x, two_y = map(int, input().split())
thr_x, thr_y = map(int, input().split())

x = one_x
y = one_y

if x == two_x:
    x = thr_x
else:
    if x == thr_x:
        x = two_x
    else:
        x = one_x

if y == two_y:
    y = thr_y
else:
    if y == thr_y:
        y = two_y
    else:
        y = one_y

print(x, y)
