import sys
input = sys.stdin.readline
""" 1890번: 점프"""

n = int(input())
graph = [[] * n for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    graph[i] = list(map(int, input().split()))
row, col = 0, 0
for i in range(row, n):
    for j in range(col, n):
        if i == n -1 and j == n - 1:
            print(dp[n - 1][n - 1])        
        d = graph[i][j]
        if i + d < n:
            dp[i + d][j] += dp[i][j]
        if j + d < n:
            dp[i][j + d] += dp[i][j]
