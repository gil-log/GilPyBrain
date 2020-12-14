# https://www.acmicpc.net/problem/4344

testCaseT = int(input())

for testCase in range(testCaseT):

    studentScores = list(map(int, input().split()))
    students = studentScores[0]
    scores = studentScores[1:]
    sum = 0
    for index in range(students):
        sum = sum + scores[index]
    averageScore = sum / students

    aboveAverageStudent = 0
    for index in range(students):
        if(scores[index] > averageScore):
            aboveAverageStudent = aboveAverageStudent + 1
    aboveAverageStudentRate = aboveAverageStudent / students * 100
    print("%.3f"%aboveAverageStudentRate+"%")