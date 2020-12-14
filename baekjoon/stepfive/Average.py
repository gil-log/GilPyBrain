# https://www.acmicpc.net/problem/1546

subjectNumber = int(input())

scores = list()
maxScore = 0
sum = 0

scores = list(map(int, input().split()))
scores.sort()

maxScore = scores[subjectNumber-1]


for i in range(0, subjectNumber):
    newScore = scores[i] / maxScore * 100
    sum = sum + newScore

average = sum / subjectNumber
print(average)

