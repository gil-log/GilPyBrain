# https://www.acmicpc.net/problem/2292
# 6 > 1
# 1 > 7
#
# 18 > 2
# 1 > 19
#
# 36 > 3
# 1 > 37
#
# 60 > 4
# 1 > 61
#
#  6 12 18 24
# 0 6 18 36 60
#
# 6 나눈게 0 ~ 1 인애들은 1칸
#
# 6 나눈게 1 ~
#
# 최대로 나눌수 있는 6의 개수를 먼저 뺀다
# 그 개수가 1 이면 1칸
#
# 1] 최대 6 뺄수잇는 횟수 0 ~ 1
# 1-1] 남은 숫자 0 ~ 1
# 1칸
#
# 2] 1 ~3
# 2-1] 남은 숫자 0 ~ 1
# 2칸
#
# 3] 3 ~ 6
# 3-1 남은 숫자 0 ~ 1
# 3칸
# 4] 6 ~ 10
# 4-1] 남은 숫자 0~1
# 4칸
#
#    2    3    4
# ~1 > ~3 > ~6 > ~10
#
# x = n(n+1)/2
# 2x = n(n+1)
import math

N = int(input())

room_count = 1

six_division = int(N / 6)
# print("6 나머지는 %i 임"%six_division)

sqrt_n = int(math.sqrt(N))

x = 0
for i in range (sqrt_n):
    x = int((i**2 + i) / 2)
    # print("x는 %a임"%x)
    if(x >= six_division):
        if ((N - x * 6) > 1):
            # print("N은 %i, X는 %i"%(N, x))
            room_count = 2

        x = i
        # print("i는 %i 임."%i)
        break

print(x + room_count)
