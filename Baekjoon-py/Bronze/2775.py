import sys
input = sys.stdin.readline
""" 2775번: 부녀회장이 될테야 """
def apart(k, n):
    if 0 <= n <= 1 or k == 0:
        return n
    else:
        if memoization[k][n] != 0:
            return memoization[k][n]
        memoization[k][n] = apart(k, n - 1) + apart(k - 1, n)
        return memoization[k][n]

t = int(input())

for _ in range(t):
    memoization = [[0] * 100 for _ in range(100)]
    k = int(input())
    n = int(input())
    print(apart(k, n))