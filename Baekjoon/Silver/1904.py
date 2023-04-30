import sys
input = sys.stdin.readline
""" 1904번: 01타일 """

dp = [0] * 1000001
dp[1] = 1; dp[2] = 2; dp[3] = 3; dp[4] = 5
n = int(input().strip())
for i in range(5, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746
    

print(dp[n])