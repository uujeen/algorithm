import sys
""" 1920번 : 수 찾기 """

def search(a, key):
    left = 0
    right = len(a) - 1
    center = (left + right) // 2
    while True:    
        if a[center] == key:
            return 1
        elif a[center] > key:
            right = center - 1
            center = (left + right) // 2
        else:
            left = center + 1
            center = (left + right) // 2
        if left > right:
            break
    return 0

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
A.sort()
for i in range(M):
    print(search(A, B[i]))
