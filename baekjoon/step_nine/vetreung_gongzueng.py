# https://www.acmicpc.net/problem/4948

N = 123456 * 2 + 1

prime_bol = [True] * N

for i in range(2, int(N**0.5) + 1):
    if prime_bol[i]:
        for j in range(2*i, N, i):
            prime_bol[j] = False

while True:
    n = int(input())
    if(n == 0): break

    if(n == 1):
        print(1)
        continue

    prime_number_count = 0

    for number in range(n+1, (n*2) +1):
        sqrt_number = int(number**0.5)

        if prime_bol[number]:
            prime_number_count += 1

    print(prime_number_count)