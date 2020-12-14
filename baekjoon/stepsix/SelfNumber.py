# https://www.acmicpc.net/problem/4673

def d(n):
    dn = n
    while n>0:
        dn = dn + n % 10
        n = int(n / 10)
    return dn

allNumber = set(range(1, 10001))
notSelfNumber = set()
for i in range (1, 10001):
    notSelfNumber.add(d(i))


selfNumber = list(allNumber - notSelfNumber)
selfNumber.sort()

for i in selfNumber:
    print(i)
