# https://www.acmicpc.net/problem/3053

import math

R = int(input())


euclid_circle = math.pi * R ** 2

taxi_circle = (R ** 2) * 2

print('%.6f' %euclid_circle)
print('%.6f' %taxi_circle)