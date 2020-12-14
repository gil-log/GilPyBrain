# https://www.acmicpc.net/problem/8958

testCaseT = int(input())

for testCase in range(testCaseT):
    OX = input()
    length = len(OX)
    score = 0
    beforeO = 0
    for index in range(length):
        thisResult = OX[index]
        if thisResult == 'O':
            if beforeO > 0:
                beforeO = beforeO + 1
                score = score + beforeO

            else:
                score = score + 1
                beforeO = 1
        else:
            beforeO = 0

    print(score)