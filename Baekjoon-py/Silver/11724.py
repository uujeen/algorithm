import sys
sys.setrecursionlimit(10000)
def dfs(v):
    visited[v] = True
    for u in vertex_list[v]:
        if not visited[u]:
            visited[u] = True
            parent[u] = v
            dfs(u)

def find(v):
    if v != parent[v]:
        parent[v] = find(parent[v])
        return parent[v]
    return v

N, M = map(int, sys.stdin.readline().split())
edge_list = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
parent = [i for i in range(N + 1)]
vertex_list = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for u, v in edge_list:
    vertex_list[u].append(v)
    vertex_list[v].append(u)

for i in range(1, N):
    if not visited[i]:
        dfs(i)

for i in range(len(parent)):
    find(i)

print(len(list(set(parent[1:]))))