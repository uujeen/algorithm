import sys
input = sys.stdin.readline
""" 9084번: 동전"""

t = int(input().rstrip())
answer = [0] * t
for k in range(t):
    n = int(input().rstrip())
    coin = list(map(int, input().split()))
    money = int(input().rstrip())
    dp = [0] * (money + 1)
    for i in range(len(coin)):
        for j in range(1, money + 1):
            if coin[i] > money:
                break
            else:
                if i == 0:
                    if coin[i] == 1:
                        dp[j] = 1
                    else:
                        if j % coin[i] == 0:
                            dp[j] = 1
                else:
                    tmp = dp[j]
                    if j - coin[i] < 0:
                        dp[j] = tmp + dp[0]
                    else:
                        dp[j] = tmp + dp[j - coin[i]]
                        if j - coin[i] == 0:
                            dp[j] += 1
    answer[k] = dp[-1]
for i in range(t):
    print(answer[i])

""" gitID: sunghwan95 성환이형 풀이 """
t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    money = int(input())
    dp = [0] * (money + 1)
    dp[0] = 1
    for coin in coins:
        for cost in range(1, money + 1):
            dp[cost] = dp[cost] + dp[cost - coin]
    print(dp[-1])