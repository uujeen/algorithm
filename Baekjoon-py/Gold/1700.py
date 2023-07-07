import sys
input = sys.stdin.readline
""" 1700번: 멀티탭 스케줄링"""

n, k = map(int, input().split())
items = list(map(int, input().split()))
plugs = []
count = 0
for idx, item in enumerate(items):
    if item in plugs:
        continue
    if len(plugs) < n:
        plugs.append(item)
        continue
    else:
        temp = []
        for plug in plugs:
            try:
                i = items[idx:].index(plug)
            except ValueError:
                i = 101
            temp.append(i)
        select = temp.index(max(temp))
        plugs[select] = items[idx]
        count += 1
print(count)