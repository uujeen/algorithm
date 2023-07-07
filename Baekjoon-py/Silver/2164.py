from collections import deque
import sys

deq = deque()

N = int(sys.stdin.readline())

for i in range(1, N + 1):
    deq.append(i)
while len(deq) != 1:
    deq.popleft()
    x = deq.popleft()
    deq.append(x)

print(deq[0])