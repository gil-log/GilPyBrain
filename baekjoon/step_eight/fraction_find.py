# https://www.acmicpc.net/problem/1193
import math

X = int(input())

if(X == 1):
    print("1/1")
    exit()

if(X == 2):
    print("1/2")
    exit()

sqrt_x = int(math.sqrt(X))

term = 0
for i in range(0, X):
    sequence = int((i**2 + i) / 2)

    if(X <= sequence):
        term = i

        break

up_flag = 1
if(term % 2 == 0):
    up_flag = 0

before_sequence = int(((term-1)**2 + term -1)/2)

sequence_term = X - before_sequence

numerator = term - sequence_term + 1
denominator = sequence_term

if(up_flag == 1):
    print("%i/%i"%(numerator, denominator))
    exit()
print("%i/%i"%(denominator, numerator))