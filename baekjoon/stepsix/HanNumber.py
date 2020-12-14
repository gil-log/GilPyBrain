# https://www.acmicpc.net/problem/1065

N = int(input())

def hanNumber(N):
    count = 99

    for i in range(100, N+1):
        units = i % 10
        tens = int(i / 10) % 10
        hundreds = int(i / 100)

        hundredsToTens = hundreds - tens
        tensToUnits = tens - units
        if(tensToUnits == hundredsToTens):
            count = count + 1

    print(count)


if N <= 99:
    print(N)
elif N <=999:
    hanNumber(N)
else:
    hanNumber(999)