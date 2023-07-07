import sys
input = sys.stdin.readline
""" 1259번 : 팰린드롬수 """

while True:
    n = list(map(int, input().rstrip()))
    flag = True
    if len(n) == 1 and n[0] == 0:
        break
    if len(n) % 2 == 1:
        for i in range(len(n) // 2):
            if n[i] != n[(-1*i) - 1]:
                flag = False
                break
    else:
        for i in range(len(n) // 2 + 1):
            if n[i] != n[(-1*i) - 1]:
                flag = False
                break
    if flag:
        print('yes')
    else:
        print('no')
