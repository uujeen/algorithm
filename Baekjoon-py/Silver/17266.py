import sys
input = sys.stdin.readline
""" 17266번 : 어두운 굴다리 """
# 시간초과
# n = int(input())
# m = int(input())
# lamps_position = list(map(int, input().split()))
# height = n // m
# while True:
#     for lamp in lamps_position:
#         for i in range(lamp - height + 1, lamp + height + 1):
#             if i >= 0 and i <= n:
#                 street_lightness[i] += 1
#     try:
#         street_lightness.index(0)
#         height += 1
#     except ValueError:
#         print(height)
#         break

N = int(input())
M = int(input())
arr = list(map(int, input().split()))

max_size = 0
for i in range(1,M):
    max_size = max(max_size, arr[i] - arr[i-1])

print(max((max_size+1)//2,arr[0] - 0, N - arr[-1]))