import sys
""" 10871번 : X보다 작은 수 """

n, x = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
count = []

for i in li:
    if i< x : count.append(i)
print(*count)