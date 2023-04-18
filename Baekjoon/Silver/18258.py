from collections import deque
import sys


deq = deque()
N = int(sys.stdin.readline())
for _ in range(N):
    order = list(map(str, sys.stdin.readline().split()))
    if order[0] == 'push':
        deq.append(int(order[1]))
    elif order[0] == 'pop':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif order[0] == 'size':
        print(len(deq))
    elif order[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    else:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])