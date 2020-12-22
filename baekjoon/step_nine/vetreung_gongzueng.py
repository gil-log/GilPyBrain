# https://www.acmicpc.net/problem/4948

while True:
    n = int(input())
    if(n == 0): break

    if(n == 1):
        print(1)
        continue

    prime_number_count = 0

    for number in range(n, (n*2) +1):
        sqrt_number = int(number**0.5)

        prime_number_flag = True
        for num in range(2, sqrt_number + 1):
            if(number % num == 0): prime_number_flag = False

        if(prime_number_flag):
            prime_number_count += 1

    print(prime_number_count)