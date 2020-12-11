# https://www.acmicpc.net/problem/2884

hour, minute = map(int, input().split())

minute = minute - 45

if minute < 0:
    minute = minute + 60
    hour = hour - 1
    if hour < 0:
        hour = hour + 24
        print(hour, minute)
    else:
        print(hour, minute)
else:
    print(hour, minute)