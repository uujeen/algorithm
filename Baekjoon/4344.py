import sys
""" 4344번 : 평균은 넘겠지 """

t = int(input())
for i in range(t):
    li = list(map(int, sys.stdin.readline().split()))
    sum = 0
    avg = 0
    count = 0
    for i in li[1:]:
        sum += i
    avg = sum/li[0]
    for i in li[1:]:
        if i > avg:
            count +=1
    print('{:.3f}%'.format(count/li[0]*100))