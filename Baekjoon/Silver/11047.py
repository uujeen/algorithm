import sys
input = sys.stdin.readline
""" 11047번: 동전 0 """

n, price = map(int, input().split())
coins = [] * n
sum = 0
for _ in range(n):
    coin = int(input())
    coins.append(coin)

for coin in coins[-1::-1]:    
    while True:
        if price - coin >= 0:
            tmp = price // coin
            price -= coin*tmp
            sum += tmp
        else:
            break
print(sum)