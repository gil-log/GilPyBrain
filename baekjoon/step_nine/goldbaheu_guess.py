# https://www.acmicpc.net/problem/9020

testCaseT = int(input())

N = 5000 * 2 + 1

seive = [True] * N

for i in range(2, int(N**0.5)+1):
    if seive[i]:
        for j in range(2 * i, N, i):
            seive[j] = False

seive[1] = False

for i in range(testCaseT):
    n = int(input())
    half_n = int(n/2)

    partition_one = half_n
    partition_two = half_n

    if(seive[half_n]):
        sum_partition = partition_one + partition_two
        if(sum_partition == n):
            print(partition_one, partition_two)
            continue

    else:

        while True:
            while not seive[partition_one]:
                partition_one -= 1

            while not seive[partition_two]:
                partition_two += 1

            sum_partition = partition_one + partition_two

            if (sum_partition == n):
                break
            elif (sum_partition > n):
                partition_one -= 1
                while not seive[partition_one]:
                    partition_one -= 1
            elif (sum_partition < n):
                partition_two += 1
                while not seive[partition_two]:
                    partition_two += 1
        print(partition_one, partition_two)


