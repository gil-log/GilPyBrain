#https://www.acmicpc.net/problem/2439

N = int(input())

blank = " "
star = "*"

for i in range(1, N+1):
    print(blank * (N-i) + star * i)