# https://www.acmicpc.net/problem/1712

A, B, C = map(int, input().split())

if(B >= C):
    print(-1)
    exit()

sales_profit = C - B
break_even_point = int(A / sales_profit) + 1

print(break_even_point)