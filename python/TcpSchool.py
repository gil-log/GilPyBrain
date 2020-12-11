a = 1 + 22
b = "gillog"

print(a)
print(b)


def sum(a, b):
    return a + b


print(sum(1, 22))

def sumMany(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum

sumOneToTen = sumMany(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(sumOneToTen)

a = "gil"
b = "log"
c = "python"

print (a+b+ c)
print((a+b) * 2)

# 튜플

tuple1 = (1, "gil")
tuple2 = (2, "log")

tuplePlus = tuple1 + tuple2

tupleMultiple = tuple1 * 3

tupleIndex = tuple1[0]

print(tuple1)
print(tuple2)
print(tuplePlus)
print(tupleMultiple)
print(tupleIndex)

print(7 / 4)
print(7 // 4)

# 딕셔너리

dictionary = {1 : "gil",
              2 : "log",
              3 : "is",
              4 : "best"}

print(dictionary[1])
print(dictionary[2])
print(dictionary[3])
print(dictionary[4])

print(dictionary)

print(dictionary.keys())

print(0 in dictionary.keys())

print(dictionary.values())

print(dictionary.items())

# list

listOne = [10, 40, 20, 50]

listTwo = [11, 51, 21, 41]

listName = ["gil", "yeo", "kim", "hong"]

listList = [listOne, listTwo, listName]

print(listOne)
print(listTwo)
print(listName)
print(listList)

listOne.sort()
listTwo.reverse()

print(listOne)
print(listTwo)

del listOne[0]

listOne.append(77)

print(listOne)


# set

myList = [22, 44, 77, 99]

setOne = set(myList)

print(setOne)

setTwo = {1, 2, 3}

setThree = {3, 3, 3}

print(setTwo, setThree, setTwo - setThree)
print(setTwo, setThree, setTwo & setThree)
print(setTwo, setThree, setTwo | setThree)


# 제어문
# if

text = "gil"
if text == "gil":
    print("gil log??")
else :
    print("oops")

# in, not in
'''
>>> a in ['a','b','c']

False

>>> 'a' in ['a','b','c']

True

>>> 'a' not in ['a','b','c']

False
'''
box =['candy','chocolate','coke']

if 'candy' in box:
    pass
    print("삼키다")


else:

    print("뱉다")


# while

meet=0

while meet<4:            # 유비가 제갈량을 방문횟수가 4보다 작을 동안 방문합니다.

    meet = meet+1        # 방문횟수 증가

    print("유비가 %d번 방문했습니다." % meet)

    if meet == 3:        # 세 번 만났기 때문에 방문을 종료함.

        print("제갈량이 유비 곁으로 갑니다.")

        break            # while 문을 빠져나온다.

# for

tempList = ['유비', '관우', '장비', '제갈량']

for i in tempList:

    print(i)

