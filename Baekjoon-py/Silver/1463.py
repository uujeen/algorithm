import sys
input = sys.stdin.readline
""" 1463번: 1로만들기"""
n = int(input().rstrip())
dp = [0] * 1000001
dp[1] = 0; dp[2] = 1; dp[3] = 1
for i in range(4, n + 1):
    if i % 6 == 0:
        dp[i] = min(dp[int(i / 2)], dp[int(i / 3)]) + 1
    elif i % 3 == 0:
        dp[i] = dp[int(i / 3)] + 1
        if dp[i - 1] < dp[int(i / 3)]:
            dp[i] = dp[i - 1] + 1
    elif i % 2 == 0:
        dp[i] = dp[int(i / 2)] + 1
        if dp[i - 1] < dp[int(i / 2)]:
            dp[i] = dp[i - 1] + 1
    else:
        dp[i] = dp[i - 1] + 1
print(dp[n])