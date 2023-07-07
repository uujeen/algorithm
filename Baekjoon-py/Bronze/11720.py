import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().rstrip()))
sum = 0
for i in a:
    sum += i
print(sum)