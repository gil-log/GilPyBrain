# https://www.acmicpc.net/problem/10871

N, X = map(int, input().split())

list = list(map(int, input().split()))

for i in range(0, N):
    if list[i] < X:
        print(list[i])
