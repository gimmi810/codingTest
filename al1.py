'''
Q. 거스름돈 동전 최소 갯수 구하기

    조건 >>
    동전 종류 : 500, 100, 50, 10

    원리 >>
    그리디 알고리즘
'''

import math

def cal_change(payment, price):
    temp = payment - price
    print(temp)
    coin = [500, 100, 50, 10]
    total = 0

    rest = {}
    for i in range(0, 4):
        rest[coin[i]] = get_count(temp, coin[i])
        total += rest[coin[i]]
        temp = get_rest(temp, coin[i])

    print(rest)
    return total

def get_count(rest, coin):
    return math.floor(rest / coin)

def get_rest(rest, coin):
    return rest % coin

payment = 5000
price = 3740
change = cal_change(payment, price)
print(change)





# 답안 예시 >>
n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)