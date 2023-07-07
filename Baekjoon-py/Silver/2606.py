import sys
""" 2606번: 바이러스 """

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
        return parent[v]
    return v

def union(u, v):
    u = find(u)
    v = find(v)
    if u != v:
        if u < v:
            parent[v] = u
        else:
            parent[u] = v

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
edge_list = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
parent = [i for i in range(n + 1)]
count = 0

for u, v in edge_list:
    union(u, v)

for i in range(1, n):
    find(i)

for i in parent[2:]:
    if find(i) == find(1):
        count += 1

print(count)