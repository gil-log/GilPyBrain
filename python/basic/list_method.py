# 리스트 메소드 정리

list_1 = ['abc', 123, 3.14, ['edf', 456], ('gh', 'st')]

print(list_1)

# ['abc', 123, 3.14, ['edf', 456], ('gh', 'st')]

# del list_1

print(list_1)

list_a = [1, 2, 3, 4, 5]

list_b = ['g', 'i', 'l', 'l', 'o', 'g']

# 파이썬 리스트 메소드

list_b.sort()

print(list_b)

list_a.sort(reverse=True)

print(list_a)

list_b.reverse()

print(list_b)

list_b.remove('l')
print(list_b)

print(list_a.pop(2))

print(list_a)

list_a.insert(3, 45)

print(list_a)

print(list_a.index(4))

print(list_b.index('l'))



print(list_a.count(5))

print(list_b.count('l'))


list_a.append(6)

print(list_a)

list_a.extend(list_b)

print(list_a)


# 내장 메소드

print(len(list_a))

print(len(list_b))

print(max(list_a))

print(max(list_b))

print(min(list_a))

print(min(list_b))

tuple_a = ('gil', 'log')

print(type(tuple_a))

list_tuple = list(tuple_a)

print(type(list_tuple))

