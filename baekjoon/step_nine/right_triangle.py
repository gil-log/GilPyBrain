# https://www.acmicpc.net/problem/4153


while True:
    a, b, c = map(int, input().split())

    if(a==0 and b==0 and c==0):
        break

    list_abc = list()

    list_abc.append(a)
    list_abc.append(b)
    list_abc.append(c)

    list_abc.sort()

    if (list_abc[0] ** 2 + list_abc[1] ** 2 == list_abc[2] ** 2):
        print('right')
        continue
    print('wrong')
