import sys
input = sys.stdin.readline
""" 12865번: 평범한 배낭 """

n, k = map(int, input().split())
stuff = [[0, 0] for _ in range(n + 1)]
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    weight, value = map(int, input().split())
    stuff[i] = [weight, value]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight, value = stuff[i][0], stuff[i][1]
        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j])
print(dp[-1][-1])