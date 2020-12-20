# collections deque 활용

from collections import deque

d = deque()
print(type(d))


# enqueue의 기능을 하는 연산 : append
for i in range(5):
    d.append(i)
print(d)

# enqueue를 리스트 왼쪽에서부터 할 수도 있다 : appendleft
d.appendleft(10)
print(d)


# 큐 중간에 요소를 삽입을 하는 연산 : insert
d.insert(5, 11)
print(d)


# 큐 왼쪽/오른쪽에 iterable한 객체를 통째로 append 하여 연장시키는 연산 : extendleft / extend
# d.extend([0, 0, 0])
print(d)
d.extendleft([0, 0, 0])
print(d)

print(d.pop())

# 스택의 pop처럼 리스트 오른쪽에서부터 요소를 제거하며 return하는 연산 : pop
for i in range(4):
    d.pop()
print(d)


# 큐의 dequeue처럼 리스트 왼쪽에서부터 요소를 제거하며 return하는 연산 : popleft
for i in range(3):
    d.popleft()
print(d)


# 작업을 완료한 후에는 일반적인 리스트처럼 이용할 수도 있다
print(list(d))