# Collections counter module 예제

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

from collections import Counter
total_shares = Counter()
for name, shares, price in portfolio:
    total_shares[name] += shares

print(total_shares['IBM'])
# 150