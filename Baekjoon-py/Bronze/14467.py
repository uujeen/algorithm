import sys
input = sys.stdin.readline

n = int(input())
cows = [-1] * 11
count = 0
for i in range(n):
    cow, tmp = map(int, input().split())
    if cows[cow] == 0:
        if cows[cow] != tmp:
            count += 1
    elif cows[cow] == 1:
        if cows[cow] != tmp:
            count += 1
    cows[cow] = tmp
print(count)