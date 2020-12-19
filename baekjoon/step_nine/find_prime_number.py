# https://www.acmicpc.net/problem/1978

N = int(input())

number_list = list(map(int, input().split()))

prime_number_count = 0
for number in number_list:
    prime_number_flag = 0
    for i in range(2, number + 1):
        if(number % i == 0):
            prime_number_flag += 1
    if(prime_number_flag == 1):
        prime_number_count += 1
    prime_number_flag = 0

print(prime_number_count)