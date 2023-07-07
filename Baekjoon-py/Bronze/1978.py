import sys
""" 1978번 : 소수 찾기 """

N = int(input())
li = list(map(int, sys.stdin.readline().split()))
li.sort()
if li[0] == 1: li.pop(0) # list.pop(idx) = 인덱스 idx에 해당하는 list 값을 삭제하고 값을 반환
length = len(li)
count = 0

for i in range(length):       
    for j in range(2,li[i]+1):
        if li[i] == j:
            count +=1
        elif li[i] % j == 0:
            break
print(count)