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