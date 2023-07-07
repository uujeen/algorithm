import sys
""" 2750번 : 수 정렬하기 """

N = int(sys.stdin.readline())
li = list(int(sys.stdin.readline()) for _ in range(N))
li.sort()
print(li)