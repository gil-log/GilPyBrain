# https://www.acmicpc.net/problem/2581

import math

M = int(input())
N = int(input())

min_prime_number = 10000
sum_prime_number = 0

for number in range(M, N+1):
    if(number == 1):
        continue
    sqrt_number = int(math.sqrt(number))
    factor = 0
    for i in range(2, sqrt_number + 1):
        if(number % i == 0):
            factor += 1
    if(factor == 0):
        sum_prime_number += number
        if(min_prime_number > number):
            min_prime_number = number

if(sum_prime_number == 0):
    print(-1)
    exit()
print(sum_prime_number)
print(min_prime_number)