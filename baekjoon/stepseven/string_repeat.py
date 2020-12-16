# https://www.acmicpc.net/problem/2675

test_case_number = int(input())

for i in range(test_case_number):
    R, S = input().split()
    R = int(R)
    P = ''
    length = len(S)
    for index in range(length):
        letter = S[index]
        for repeat in range(R):
            P = P + letter
    print(P)