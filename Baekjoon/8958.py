import sys
""" 8958번 : OX퀴즈 """

t = int(input())
for _ in range(t):
    li = list(map(str,sys.stdin.readline()))
    count = 0
    sum = 0
    for i in li:
        if i =='O':
            count += 1
            sum += count
        else :
            count = 0
    print(sum)