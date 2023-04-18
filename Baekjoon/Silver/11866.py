from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
deq = deque()

for i in range(1, N + 1):
    deq.append(i)
result = []
count = 0
target = 1
while count != N:
    if target % K == 0:
        for _ in range(K-1):
            x = deq.popleft()
            deq.append(x)
        a = deq.popleft()
        result.append(a)
        count += 1
    target += 1

print('<', end='')
print(*result, sep=', ', end='')
print('>')