import sys
""" 2805번 : 나무 자르기 (이분 탐색) """
N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
left, right = 1, max(trees)

while left <= right:
    mid = (left + right) // 2
    sum_of_trees = 0

    for i in trees:
        if i >= mid:
            sum_of_trees += i - mid

    if sum_of_trees >= M:
        left = mid + 1
    else:
        right = mid - 1
print(right)