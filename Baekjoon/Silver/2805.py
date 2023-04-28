import sys
""" 2805번 : 나무 자르기 (이분 탐색) """
n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
left, right = 0, max(trees)

def check(mid, n, m, trees):
    sum = 0
    for i in range(n):
        if trees[i] >= mid:
            sum += trees[i] - mid
    return sum >= m

while left + 1 < right:
    mid = (left + right) // 2
    if check(mid, n, m, trees):
        left = mid
    else:
        right = mid
print(left)