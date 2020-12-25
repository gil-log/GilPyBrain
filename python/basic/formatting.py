# 포매팅

## 문자열 포매팅
name = 'IBM'
shares = 100
price = 91.1
print(f'{name:>10s} {shares:>10d} {price:>10.2f}')
# '       IBM        100      91.10'

## 딕셔너리 포매팅
s = {
    'name': 'IBM',
    'shares': 100,
    'price': 91.1
}

print('{name:>10s} {shares:10d} {price:10.2f}'.format_map(s))
# '       IBM        100      91.10'


## format() method
print('{name:>10s} {shares:10d} {price:10.2f}'.format(name='IBM', shares=100, price=91.1))
# '       IBM        100      91.10'

print('{:10s} {:10d} {:10.2f}'.format('IBM', 100, 91.1))
# '       IBM        100      91.10'

## C 스타일 포매팅
print('The value is %d' % 3)
# 'The value is 3'

print('%5d %-5d %10d' % (3,4,5))
# '    3 4              5'

print('%0.2f' % (3.1415926,))
# '3.14'


## 바이너리

print(b'%s has %d messages' % (b'Dave', 37))
# b'Dave has 37 messages'