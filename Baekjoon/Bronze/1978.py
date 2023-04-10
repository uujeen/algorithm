import sys
""" 1978번 : 소수 찾기 """

t = int(input())
li = list(map(int,sys.stdin.readline().split()))
count = 0
for i in range(t):
    for j in range(2, li[i]):
        while True:
            if li[j] % (j-1) == 0:
                break
            else:
                count +=1