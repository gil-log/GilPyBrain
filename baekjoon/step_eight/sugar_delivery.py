# https://www.acmicpc.net/problem/2839

N = int(input())

max_five_kilogram_bag = int(N / 5)
minus_max_five_kilogram = N - max_five_kilogram_bag * 5
if (minus_max_five_kilogram == 3 or minus_max_five_kilogram == 0):
    print(max_five_kilogram_bag + int(minus_max_five_kilogram / 3))
    exit()

five_kilogram_bag = 0
three_kilogram_bag = 0
while N > 0:
    N = N - 3
    three_kilogram_bag = three_kilogram_bag + 1
    if(N % 5 == 0):
        five_kilogram_bag = int(N / 5)
        print(five_kilogram_bag + three_kilogram_bag)
        exit()

print(-1)
