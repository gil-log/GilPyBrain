# 예외처리

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")

try:
    a = [1,2]
    4/0
    print(a[3])
except (ZeroDivisionError, IndexError) as e:
    print(e)

try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()