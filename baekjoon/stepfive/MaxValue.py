# https://www.acmicpc.net/problem/2562

listA = list()

for i in range(9):
    listA.append(int(input()))

maxValue = max(listA)
maxValueIndex = listA.index(maxValue)

print(maxValue)
print(maxValueIndex + 1)