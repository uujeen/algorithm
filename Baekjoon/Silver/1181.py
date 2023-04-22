import sys

N = int(sys.stdin.readline())
a = []
arr = []
for i in range(N):
    a.append(str(sys.stdin.readline()))

a = list(set(a))
a.sort()
for i in range(len(a)):
    arr.append([len(a[i]),i])

arr.sort()
for i in range(len(arr)):
    idx = arr[i][1]
    print(str(a[idx]), end='')