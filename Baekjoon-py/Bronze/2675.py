import sys
""" 2675번 : 문자열 반복 """

t = int(input())
for i in range(t):
    C = list(map(str, sys.stdin.readline().split()))
    S = C[1]
    li = ''
    for i in S:
        li += i*int(C[0])
    print(li)