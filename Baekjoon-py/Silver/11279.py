from  heapq import heappush, heappop
import sys

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap)[1])
    else:
        heappush(heap, (-x, x))