# https://www.acmicpc.net/problem/10809

S = input()

result = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
          -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

length = len(S)
for i in range(length):
    alphabet_index = ord(S[i]) - 97
    if(result[alphabet_index] == -1):
        result[alphabet_index] = i

for i in result:
    print(i, end=' ')